import os
import uvicorn
import logging
import secrets

from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles

from fastapi import HTTPException, status
from fastapi.responses import FileResponse
from fastapi import Request, HTTPException

import server.base as model

logging.basicConfig(level=logging.DEBUG, filename="monitor.log")
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root_index():
    return FileResponse("dist/index.html")


@app.get("/index.html")
async def root_index1():
    return FileResponse("dist/index.html") 

@app.on_event('startup')
async def startup():
    model.connect()

#app.mount("/css", StaticFiles(directory="dist/css"), name="dict")
app.mount("/js", StaticFiles(directory="dist/js"), name="dict")
app.mount("/data", StaticFiles(directory="data"), name="dict")


@app.get('/api/event/{timestamp}')
async def get_event(request: Request):
    timestamp = request.path_params.get('timestamp')
    return await model.get_event(timestamp)


@app.get('/api/events_list')
async def get_events_list(request: Request):
    
    return await model.get_events_list()  


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")