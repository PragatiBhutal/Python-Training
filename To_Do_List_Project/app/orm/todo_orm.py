from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ToDo(Base):
    """
        ORM model for the ToDo table in the database.
    """
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=50))
    description = Column(String(length=200))
    priority = Column(String)
    is_completed = Column(Boolean, default=False)
    due_date = Column(DateTime, default=datetime.utcnow)
