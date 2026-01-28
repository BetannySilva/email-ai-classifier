import os
import json
import re
from google import genai
from dotenv import load_dotenv

load_dotenv()

gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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

    response = gemini.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    raw = response.text.strip()

    match = re.search(r"\{.*\}", raw, re.DOTALL)

    if not match:
        return {"categoria": "Erro", "resposta": raw}

    try:
        return json.loads(match.group())
    except:
        return {"categoria": "Erro", "resposta": raw}
