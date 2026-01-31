import os, json, re
from google import genai
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "models/gemini-flash-latest"


def classify_and_reply(email_text: str):
    prompt = f"""
Você é um assistente de uma empresa do setor financeiro.

Classifique o email como:
- Produtivo
- Improdutivo

Depois gere uma resposta profissional e educada.

Email:
\"\"\"{email_text}\"\"\"

Responda SOMENTE com um JSON válido:
{{"categoria": "...", "resposta": "..."}}
"""

    def call():
        return client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

    try:
        with ThreadPoolExecutor(max_workers=1) as ex:
            future = ex.submit(call)
            response = future.result(timeout=12)

        raw = response.text.strip()
        match = re.search(r"\{.*\}", raw, re.DOTALL)

        if not match:
            return {"categoria": "Erro", "resposta": raw}

        return json.loads(match.group())

    except TimeoutError:
        return {
            "categoria": "Timeout",
            "resposta": "A IA demorou demais para responder."
        }
    except Exception as e:
        return {
            "categoria": "Erro",
            "resposta": str(e)
        }
        

    except Exception as e:
        msg = str(e)

        # LIMITE DE QUOTA / RATE LIMIT
        if "RESOURCE_EXHAUSTED" in msg or "429" in msg or "quota" in msg.lower():
            return {
                "categoria": "Limite Atingido",
                "resposta": (
                    "O limite diário da IA foi atingido.\n\n"
                    "Isso acontece porque a versão gratuita do Gemini tem uma cota restrita.\n"
                    "Tente novamente mais tarde."
                )
            }

        # API desativada
        if "PERMISSION_DENIED" in msg or "SERVICE_DISABLED" in msg:
            return {
                "categoria": "API Desativada",
                "resposta": (
                    "A API do Gemini não está habilitada neste projeto.\n"
                    "Ative o serviço 'Generative Language API' no Google Cloud."
                )
            }

        # ERRO GENÉRICO
        return {
            "categoria": "Erro",
            "resposta": msg
        }
