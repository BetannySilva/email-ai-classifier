# from fastapi import FastAPI
# from pydantic import BaseModel

# from app.classifier import email_classifier
# from app.ia import classify_and_reply
# from app.nlp import process_email

# from dotenv import load_dotenv
# load_dotenv()

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"status": "API rodando com sucesso"}

# class Email(BaseModel):
#     email: str

# @app.post("/receive-email/")
# def receive_email(data: Email):
#     email_text = data.email.replace("\n", " ")
#     email_text = data.email
#     processed_email = process_email(email_text)
#     categoria_text = email_classifier(processed_email)

#     ai_result = classify_and_reply(email_text)

#     return {
#         "mensagem_recebida": email_text,
#         "mensagem_processada": processed_email,
#         "categoria_regra": categoria_text,
#         "categoria_ia": ai_result["categoria"],
#         "resposta": ai_result["resposta"]
#     }


from fastapi import FastAPI
from pydantic import BaseModel
from app.ia import classify_and_reply

app = FastAPI(title="Email AI Classifier")

class EmailRequest(BaseModel):
    email: str

@app.post("/classificar")
def classificar(req: EmailRequest):
    result = classify_and_reply(req.email)
    return result
