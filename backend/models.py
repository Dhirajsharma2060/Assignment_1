from sqlalchemy import Column, Integer, String, Boolean
from db import Base

class Task(Base):
    """
    SQLAlchemy model for the Task table.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)