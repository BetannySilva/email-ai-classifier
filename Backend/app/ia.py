import os, json, re
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configura a chave da API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Modelo leve e rápido
model = genai.GenerativeModel("gemini-1.5-flash")

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

    try:
        response = model.generate_content(prompt)
        raw = response.text.strip()

        # Extrai apenas o JSON
        match = re.search(r"\{.*\}", raw, re.DOTALL)

        if not match:
            return {"categoria": "Erro", "resposta": raw}

        return json.loads(match.group())

    except Exception as e:
        msg = str(e)

        # Limite de quota
        if "RESOURCE_EXHAUSTED" in msg or "429" in msg or "quota" in msg.lower():
            return {
                "categoria": "Limite Atingido",
                "resposta": (
                    "A cota gratuita da IA foi atingida.\n"
                    "Tente novamente mais tarde."
                )
            }

        # API desativada
        if "PERMISSION_DENIED" in msg or "SERVICE_DISABLED" in msg:
            return {
                "categoria": "API Desativada",
                "resposta": (
                    "A API do Gemini não está habilitada.\n"
                    "Ative a Generative Language API no Google Cloud."
                )
            }

        return {
            "categoria": "Erro",
            "resposta": msg
        }
