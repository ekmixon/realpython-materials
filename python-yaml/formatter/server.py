"""
Running the backend:
$ uvicorn formatter:app

Viewing the frontend:
http://127.0.0.1:8000/
"""

from typing import Optional

import yaml
from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

TEST_DATA = {
    "person": {
        "name_latin": "Ivan",
        "name": "Иван",
        "age": 42,
    }
}


class Parameters(BaseModel):
    # Boolean flags:
    allow_unicode: bool = False
    canonical: bool = False
    default_flow_style: bool = False
    explicit_end: bool = False
    explicit_start: bool = False
    sort_keys: bool = True

    # Valued parameters:
    indent: Optional[int] = None
    width: Optional[int] = None
    default_style: Optional[str] = None
    encoding: Optional[str] = None
    line_break: Optional[str] = None
    version: Optional[list] = None


app = FastAPI()
app.mount("/static", StaticFiles(directory="static/"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("views/index.html", "rb") as file:
        return file.read()


@app.post("/")
async def serialize(parameters: Parameters):
    try:
        serialized = yaml.dump(TEST_DATA, **vars(parameters))
        return repr(serialized) if isinstance(serialized, bytes) else serialized
    except Exception as ex:
        return JSONResponse(str(ex), status_code=400)
