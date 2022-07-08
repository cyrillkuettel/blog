from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import FileResponse

from app.core.settings import Paths

import logging

app = FastAPI()
templates = Jinja2Templates(directory=str(Paths.templates.resolve()))


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return FileResponse(Paths.NOT_FOUND_404)


@app.get("/app/matterjs")
async def root():
    return {"message": "Hello World"}


@app.get("/app/templates")
async def main(request: Request):
    bla = "it works :)"
    return templates.TemplateResponse(
        "index.html", {"request": request, "bla": bla, })  #
