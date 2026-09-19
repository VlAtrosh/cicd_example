from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>IdeaCRAFT</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="card">
            <h1>Привет!</h1>
            <p>Добро пожаловать в IdeaCRAFT</p>
            <img src="/static/raf.jpg" alt="raf">
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
