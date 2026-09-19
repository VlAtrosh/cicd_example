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
            <img src="/static/raf.jpg" alt="raf" class="hero-img">
            <h1>Привет!</h1>
            <p>Visca Barca</p>
            <button class="btn" onclick="showVideo()">Показать видео</button>

            <div id="video-block" class="video-hidden">
                <video id="edit-video" controls width="100%">
                    <source src="/static/edit.mp4" type="video/mp4">
                    Твой браузер не поддерживает видео.
                </video>
            </div>
        </div>

        <script>
            function showVideo() {
                const block = document.getElementById('video-block');
                block.classList.toggle('video-hidden');
                if (!block.classList.contains('video-hidden')) {
                    document.getElementById('edit-video').play();
                }
            }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
