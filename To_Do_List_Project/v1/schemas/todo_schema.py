from datetime import datetime

from pydantic import BaseModel, Field


class ToDoBaseSchema(BaseModel):
    """
        Base schema for ToDo objects with common fields.
    """
    title: str = Field( min_length=3, max_length=100)
    description: str = Field(min_length=10, max_length=500)
    priority: str
    is_completed: bool
    due_date: datetime


class ToDoPostPutInputSchema(ToDoBaseSchema):
    """
    Schema for creating or updating a TODO Task.
    """
    pass


class ToDoResponseSchema(ToDoBaseSchema):
    """
       Schema for the response of a ToDo task, including the ID.
     Attributes:
      id (int): The unique identifier of the task.
    """
    id: int

