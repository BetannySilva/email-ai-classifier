from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.ia import classify_and_reply

app = FastAPI()

# Torna a pasta "static" acessível no navegador
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura a pasta de templates HTML
templates = Jinja2Templates(directory="templates")

# Modelo de dados recebido no POST
class EmailRequest(BaseModel):
    email: str
# Rota principal que carrega o site
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
# Rota simples para testar se a API está online
@app.get("/ping")
def ping():
    return {"status": "ok"}
# Rota que recebe o email e chama a IA
@app.post("/classificar")
def classificar(req: EmailRequest):
    return classify_and_reply(req.email)
