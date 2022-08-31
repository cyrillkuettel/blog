from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.core.settings import Paths
from hn import HN

app = FastAPI()
app.mount("/app/templates", StaticFiles(directory=Paths.templates.resolve()), name="stati")

templates = Jinja2Templates(directory=str(Paths.templates.resolve()))
angry_birds_template = Jinja2Templates(directory=str(Paths.angry_birds_template_root.resolve()))


@app.get("/app/api")
async def api(request: Request):
    hn = HN()

    class Story:
        def __init__(self, rank, title):
            self.rank = rank
            self.title = title

    stories: list[Story] = []
    for story in hn.get_stories(story_type='newest', limit=30):
        stories.append(Story(story.rank, story.title))

    return stories


@app.get("/app/matterjs")
async def matterjs(request: Request):
    return angry_birds_template.TemplateResponse("index.html", {"request": request})


@app.exception_handler(404)
async def custom_404_handler(_, __):
    #  Display the NGINX 404 page
    return FileResponse(Paths.NOT_FOUND_404)
