from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pathlib import Path
import logging

current_file = Path(__file__)
current_file_dir = current_file.parent  # /code/app
TEMPLATES = current_file_dir / "templates"

app = FastAPI()
templates = Jinja2Templates(directory=str(TEMPLATES.resolve()))


@app.get("/matterjs")
async def root():
    return {"message": "Hello World"}


@app.get("/main")
async def main():
    bla = "it works :)"
    return templates.TemplateResponse(
        "index.html", {"bla": bla, })  #
