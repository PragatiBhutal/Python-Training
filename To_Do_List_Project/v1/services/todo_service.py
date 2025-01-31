from sqlalchemy.orm import Session
from v1.repository.todo_repository import ToDoRepository


class ToDoService:
    """
    Service layer for handling business logic related to ToDo tasks.
    """
    def __init__(self, db: Session):
        """
        Initialize the service with a database session.
        """
        self.repository = ToDoRepository(db)

    def create_task(self, task):
        """
        Create a new ToDo task using the repository.
        """
        return self.repository.create_task(task)

    def get_all_tasks(self):
        """
        Retrieve all ToDo tasks using the repository.
        """
        return self.repository.get_all_tasks()

    def get_task_by_id(self, task_id: int):
        """
        Retrieve a specific ToDo task by its ID using the repository.
        """
        return self.repository.get_task_by_id(task_id)

    def update_task(self, task_id: int, task):
        """
        Update a specific ToDo task by its ID using the repository.
        """
        return self.repository.update_task(task_id, task)

    def delete_task(self, task_id: int):
        """
        Delete a specific ToDo task by its ID using the repository.
        """
        return self.repository.delete_task(task_id)
