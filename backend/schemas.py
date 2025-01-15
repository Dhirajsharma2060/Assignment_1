from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NewTaskBase(BaseModel):
    """
    Base schema for NewTask.
    """
    name: str
    status: bool = False

class NewTaskCreate(NewTaskBase):
    """
    Schema for creating a new NewTask.
    """
    pass

class NewTaskUpdate(NewTaskBase):
    """
    Schema for updating an existing NewTask.
    """
    pass

class NewTask(NewTaskBase):
    """
    Schema for reading a NewTask.
    """
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes  = True