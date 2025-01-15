from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from db import Base

class NewTask(Base):
    """
    SQLAlchemy model for the NewTask table.
    """
    __tablename__ = "new_tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())