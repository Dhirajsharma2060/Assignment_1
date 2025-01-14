from fastapi import FastAPI, HTTPException, Depends
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session
from typing import List
import uvicorn
from db import get_db, engine, test_db_connection
from models import Base, Task as TaskModel
from schemas import Task as TaskSchema, TaskCreate
from exceptions import http_exception_handler, validation_exception_handler, generic_exception_handler

app = FastAPI()

# Test the database connection
test_db_connection()

# Create the database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    """
    Root endpoint.
    """
    return {"message": "Welcome to the To-Do App"}

@app.get("/tasks", response_model=List[TaskSchema])
def read_tasks(db: Session = Depends(get_db)):
    """
    Retrieve all tasks.
    """
    return db.query(TaskModel).all()

@app.post("/tasks", response_model=TaskSchema)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.
    """
    db_task = TaskModel(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.patch("/tasks/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    """
    Update an existing task.
    """
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db_task.title = task.title
    db_task.description = task.description
    db_task.completed = task.completed
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}", response_model=TaskSchema)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task.
    """
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return db_task

@app.get("/tasks/{task_id}", response_model=TaskSchema)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a task by ID.
    """
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# Global exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
