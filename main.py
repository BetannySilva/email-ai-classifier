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

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.ia import classify_and_reply

app = FastAPI(title="Email AI Classifier")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class EmailRequest(BaseModel):
    email: str
@app.get("/ping")
def ping():
    return {"status": "ok"}


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/classificar")
def classificar(req: EmailRequest):
    return classify_and_reply(req.email)
