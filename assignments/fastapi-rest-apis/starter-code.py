from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import uuid4

app = FastAPI()

class Task(BaseModel):
    id: str
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    completed: bool = False

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    completed: Optional[bool] = False

# In-memory store
tasks = []  # type: List[Task]

@app.get('/tasks', response_model=List[Task])
def list_tasks(completed: Optional[bool] = None, search: Optional[str] = None):
    results = tasks
    if completed is not None:
        results = [t for t in results if t.completed == completed]
    if search:
        results = [t for t in results if search.lower() in t.title.lower()]
    return results

@app.get('/tasks/{task_id}', response_model=Task)
def get_task(task_id: str):
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail='Task not found')

@app.post('/tasks', response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    new_task = Task(id=str(uuid4()), title=task.title, description=task.description, completed=task.completed or False)
    tasks.append(new_task)
    return new_task

@app.put('/tasks/{task_id}', response_model=Task)
def update_task(task_id: str, task: TaskCreate):
    for idx, t in enumerate(tasks):
        if t.id == task_id:
            updated = Task(id=t.id, title=task.title, description=task.description, completed=task.completed or False)
            tasks[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail='Task not found')

@app.delete('/tasks/{task_id}', status_code=204)
def delete_task(task_id: str):
    for idx, t in enumerate(tasks):
        if t.id == task_id:
            tasks.pop(idx)
            return
    raise HTTPException(status_code=404, detail='Task not found')

# If executed directly, allow running with `python starter-code.py` for quick dev
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('starter-code:app', host='127.0.0.1', port=8000, reload=True)
