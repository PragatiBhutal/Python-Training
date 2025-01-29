from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database.todo_db import SessionLocal
from app.schemas.todo_schema import ToDoResponseSchema, ToDoPostPutInputSchema
from app.services.todo_service import ToDoService

router = APIRouter()

db: Session = SessionLocal()


@router.post("/add", response_model=ToDoResponseSchema)
def create_task(task: ToDoPostPutInputSchema):
    """
    Create a new ToDo task.
    """
    service = ToDoService(db)
    return service.create_task(task)


@router.get("/view all", response_model=list[ToDoResponseSchema])
def get_all_tasks():
    """
    Retrieve all ToDo tasks.
    """
    service = ToDoService(db)
    return service.get_all_tasks()


@router.get("/view", response_model=ToDoResponseSchema)
def get_task_by_id(task_id: int):
    """
    Retrieve a specific ToDo task by its ID.
    """
    service = ToDoService(db)
    task = service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/update", response_model=ToDoResponseSchema)
def update_task(task_id: int, task: ToDoPostPutInputSchema):
    """
    Update a specific ToDo task by its ID.
    """
    service = ToDoService(db)
    updated_task = service.update_task(task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/remove", response_model=ToDoResponseSchema)
def delete_task(task_id: int):
    """
    Delete a specific ToDo task by its ID.
    """
    service = ToDoService(db)
    deleted_task = service.delete_task(task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task
