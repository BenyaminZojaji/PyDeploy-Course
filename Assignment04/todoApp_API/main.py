from typing import Optional
from time import time as timeNow
from datetime import time as timeFormat
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import database


app = FastAPI()


class BaseTask(BaseModel):
    title: str

class Task(BaseTask):
    id: Optional[int] = None
    description: str
    time: timeFormat = None
    status: bool

class ReturnTask(BaseTask):
    pass

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.middleware("http")
async def log_middleware(request, call_next):
    start_time = timeNow()
    response = await call_next(request)
    process_time = timeNow() - start_time
    response.headers["Process-Time"] = f'Request {request.url} processed in {process_time} seconds.'
    return response

@app.get("/")
async def root():
    return "This is an API for Todo Application powered by FastAPI and sqlite to save tasks."

@app.get("/task")
async def read_task(id: Optional[int] = None):
    if database.search_task(id) is False and id is not None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID does not exist")
    return database.get_task(id)

@app.post("/task", response_model=ReturnTask)
async def add_task(task: Task):
    if task.id == None:
        task.id = database.count_tasks() + 1
    try:
        database.add_task(int(task.id), str(task.title), str(task.description), str(task.time), str(task.status))
        return task
    except:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Required unique ID")
    

@app.put("/task")
async def update_task(id: int, newTask: Task):
    if database.search_task(id) is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID does not exist")
    database.update_task(int(id), str(newTask.title), str(newTask.description), str(newTask.time), str(newTask.status))

@app.delete("/task")
async def delete_task(id: int):
    if database.search_task(id) is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID does not exist")
    database.delete_task(id)
