from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from .core.settings import Paths

import logging

app = FastAPI()
templates = Jinja2Templates(directory=str(Paths.templates.resolve()))


@app.get("/matterjs")
async def root():
    return {"message": "Hello World"}


@app.get("/templates")
async def main(request: Request):
    bla = "it works :)"
    return templates.TemplateResponse(
        "index.html", {"request": request, "bla": bla, })  #
