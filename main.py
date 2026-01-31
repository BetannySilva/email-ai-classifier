
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

from mangum import Mangum
handler = Mangum(app)
