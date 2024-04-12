from typing import Optional
from datetime import time as timeFormat
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status
import app.database as database


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
    elif not database.search_task(task.id):
        database.add_task(int(task.id), str(task.title), str(task.description), str(task.time), str(task.status))
        return task
    else:
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
