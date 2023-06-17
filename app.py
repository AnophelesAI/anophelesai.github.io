from uvicorn import run as uvicorn_run
from fastapi import FastAPI, Request, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uuid import uuid4
from experta import Fact
from main import DB ,  Patient, HaveMalaria, Name_Checked
app = FastAPI()
templates = Jinja2Templates(directory="static")

@app.post("/post/")
async def formPage(
    request: Request,
):
    
    try:
        name = str(uuid4())
        engine = HaveMalaria()
        engine.reset()
        Name_Checked[name] = False
        DB[name] = "You have no symptoms. Based on that, you are considered healthy."
        selectedoptions = { x.split(':')[0] : x.split(':')[1].strip() == 'true'  for x in request.cookies['choices'].split("&")}
        engine.declare(Patient(name=name, **selectedoptions))
        engine.run()
        return templates.TemplateResponse("Result.html", {"result": DB.get(name), "request": request,})
    except Exception as e:
        return templates.TemplateResponse("Result.html", {"result": "No result.", "request": request,})

app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn_run("app:app", host="0.0.0.0", port=8001, reload=True)
