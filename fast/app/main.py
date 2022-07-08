from fastapi import FastAPI

app = FastAPI()


@app.get("/matterjs")
async def root():
    return {"message": "Hello World"}
