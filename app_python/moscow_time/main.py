import os.path
from datetime import datetime

import json
import requests
from fastapi import FastAPI
from os import path
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def get_time():
    """Make GET request to WorldTimeAPI about current Moscow Time and return it.

    Returns
    -------
    html
        an html page with current Moscow time or with error code.
    """
    style = """
        \"background-image: url('https://wallpaperaccess.com/full/372581.jpg');
        display: flex;
        justify-content: center;
        text-align: center;
        flex-direction: column;
        color: white;
        font-size: 30px;\"
    """
    html_content = """
        <html>
            <head>
                <title>Moscow Current Time</title>
            </head>
            <body style=%s>
                <h1>Moscow time</h1>
                <h1>%s</h1>
            </body>
        </html>
        """
    url = "http://worldtimeapi.org/api/timezone/Europe/Moscow"
    response = requests.get(url)
    if response.status_code == 200:
        pattern = "%Y-%m-%dT%H:%M:%S.%f%z"
        date = datetime.strptime(response.json()["datetime"], pattern)
        time = f"{date.hour}:{date.minute}:{date.second}"
        await write_time(time)
        return HTMLResponse(content=html_content % (style, time),
                            status_code=200)
    else:
        error = f"Error: {response.status_code}"
        return HTMLResponse(content=html_content % (style, error),
                            status_code=404)


@app.get("/visits")
async def get_visits():
    if not path.exists('./app_python/data/visits.json'):
        with open('visits.json', 'w') as f:
            pass
    def iterfile():
        with open("./app_python/data/visits.json", mode="r") as file:
            yield from file
    return StreamingResponse(iterfile())


async def write_time(time):
    doesExist = os.path.exists("/app_python/data/")
    if not doesExist:
        os.makedirs("./app_python/data")
        with open("./app_python/data/visits.json", "a") as file:
            file.write(f"Accessed at: {time}\n")
    else:
        with open("./app_python/data/visits.json", "a") as file:
            file.write(f"Accessed at: {time}\n")
