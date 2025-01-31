from sqlalchemy.orm import Session

from v1.orm.todo_orm import ToDo
from v1.schemas.todo_schema import ToDoPostPutInputSchema


class ToDoRepository:
    """
    Repository layer for interacting with the ToDo table in the database.
    """
    def __init__(self, db: Session):
        """
        Initialize the repository with a database session.
        """
        self.db = db

    def create_task(self, task: ToDoPostPutInputSchema):
        """
        Create a new ToDo task in the database.
        """
        db_task = ToDo(
            title=task.title,
            description=task.description,
            priority=task.priority,
            is_completed=task.is_completed,
            due_date=task.due_date
        )
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_all_tasks(self):
        """
        Retrieve all ToDo tasks from the database.
        """
        return self.db.query(ToDo).all()

    def get_task_by_id(self, task_id: int):
        """
        Retrieve a specific ToDo task by its ID.
        """
        return self.db.query(ToDo).filter(ToDo.id == task_id).first()

    def update_task(self, task_id: int, task: ToDoPostPutInputSchema):
        """
        Update a ToDo task by its ID.
        """
        db_task = self.db.query(ToDo).filter(ToDo.id == task_id).first()
        if db_task:
            db_task.title = task.title
            db_task.description = task.description
            db_task.priority = task.priority
            db_task.is_completed = task.is_completed
            db_task.due_date = task.due_date
            self.db.commit()
            self.db.refresh(db_task)
        return db_task

    def delete_task(self, task_id: int):
        """
        Delete a ToDo task by its ID.
        """
        db_task = self.db.query(ToDo).filter(ToDo.id == task_id).first()
        if db_task:
            self.db.delete(db_task)
            self.db.commit()
        return db_task
