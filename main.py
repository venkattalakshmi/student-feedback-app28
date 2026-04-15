from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Correct template path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Temporary storage
feedback_list = []

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "feedbacks": feedback_list
        }
    )

@app.post("/submit")
def submit(name: str = Form(...), feedback: str = Form(...)):
    feedback_list.append({
        "name": name,
        "feedback": feedback
    })
    return RedirectResponse(url="/", status_code=303)
