from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return {"msg": "Visca Barca!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
