from pydantic import BaseModel, constr
from typing import Optional

DescriptionStr = constr(max_length=500)

class TaskBase(BaseModel):
    """
    Base schema for Task.
    """
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskCreate(TaskBase):
    """
    Schema for creating a new Task.
    """
    pass

class Task(TaskBase):
    """
    Schema for reading a Task.
    """
    id: int

    class Config:
        from_attributes = True