from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head><title>Моя страница</title></head>
        <body>
            <h1>Привет!</h1>
            <img src="/static/raf.jpg" alt="cat" width="400">
        </body>
    </html>
    """


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
