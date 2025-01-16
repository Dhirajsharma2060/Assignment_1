from fastapi import FastAPI, HTTPException, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import uvicorn
from db import get_db, engine, test_db_connection
from models import Base, NewTask as TaskModel
from schemas import NewTask as TaskSchema, NewTaskCreate as TaskCreate, NewTaskUpdate as TaskUpdate
from exceptions import http_exception_handler, validation_exception_handler, generic_exception_handler

app = FastAPI()

# Configure CORS
origins = [
    #"https://frontend-part-oj8w.onrender.com/",  # React development server
    # "https://todo-app-myh1.onrender.com",  # Deployed backend
    "https://frontend-5w9c.onrender.com",
    "https://frontend-part-oj8w.onrender.com/",
    "https://assignment-1-lm22.onrender.com",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test the database connection
test_db_connection()

# Create the database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    """
    Root endpoint.
    """
    return {"message": "Welcome to the Todo App"}

@app.get("/tasks/", response_model=List[TaskSchema])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve all tasks.
    """
    tasks = db.query(TaskModel).offset(skip).limit(limit).all()
    return tasks

@app.post("/tasks/", response_model=TaskSchema)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.
    """
    db_task = TaskModel(name=task.name, status=task.status)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.patch("/tasks/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    """
    Update an existing task.
    """
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db_task.name = task.name
    db_task.status = task.status
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

@app.delete("/tasks/", response_model=List[TaskSchema])
def delete_all_tasks(db: Session = Depends(get_db)):
    """
    Delete all tasks.
    """
    tasks = db.query(TaskModel).all()
    for task in tasks:
        db.delete(task)
    db.commit()
    return tasks

# Global exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
