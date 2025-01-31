import csv
from io import StringIO

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import StreamingResponse

from v1.database.todo_db import SessionLocal
from v1.schemas.todo_schema import ToDoResponseSchema, ToDoPostPutInputSchema
from v1.services.todo_service import ToDoService

router = APIRouter()

db: Session = SessionLocal()


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


@router.post("/add", response_model=ToDoResponseSchema)
def create_task(task: ToDoPostPutInputSchema):
    """
    Create a new ToDo task.
    """
    service = ToDoService(db)
    return service.create_task(task)


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


@router.get("/todos/{task_id}/csv", response_class=StreamingResponse)
def get_todo_csv(task_id: int):
    """
    Download a specific ToDo task as a CSV file based on ID.
    """
    service = ToDoService(db)
    task = service.get_task_by_id(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Title", "Description", "Priority", "Is Completed", "Due Date"])
    writer.writerow([task.id, task.title, task.description, task.priority, task.is_completed, task.due_date])
    return StreamingResponse(output, media_type="text/csv",
                             headers={"Content-Disposition": f"attachment; filename=todo_{task_id}.csv"})


@router.get("/todos/csv", response_class=StreamingResponse)
def get_all_todos_csv():
    """
    Download all ToDo tasks as a CSV file.
    """
    service = ToDoService(db)
    tasks = service.get_all_tasks()

    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found")

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Title", "Description", "Priority", "Is Completed", "Due Date"])

    for task in tasks:
        writer.writerow([task.id, task.title, task.description, task.priority, task.is_completed, task.due_date])

    return StreamingResponse(output, media_type="text/csv",
                             headers={"Content-Disposition": "attachment; filename=todos.csv"})
