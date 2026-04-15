from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Temporary storage (list)
feedback_list = []

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "feedbacks": feedback_list})

from fastapi.responses import RedirectResponse

@app.post("/submit")
def submit(name: str = Form(...), feedback: str = Form(...)):
    feedback_list.append({"name": name, "feedback": feedback})
    return RedirectResponse(url="/", status_code=303)