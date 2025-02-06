from sqlalchemy.orm import Session
from models import Todos
from schemas import TodoRequest

def create_todo(db: Session, todo_request: TodoRequest):
    """
    Create a new todo item in the database.

    Args:
        db (Session): The database session.
        todo_request (TodoRequest): The request object containing todo details.

    Returns:
        Todos: The created todo item.
    """
    todo = Todos(**todo_request.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def read_todos(db: Session, complete: bool):
    """
    Retrieve todo items from the database.

    Args:
        db (Session): The database session.
        complete (bool): Filter todos by completion status. If None, return all todos.

    Returns:
        list: A list of todo items.
    """
    if complete is None:
        return db.query(Todos).all()
    else:
        return db.query(Todos).filter(Todos.complete == complete).all()

def update_todo(db: Session, id: int, todo: TodoRequest):
    """
    Update an existing todo item in the database.

    Args:
        db (Session): The database session.
        id (int): The ID of the todo item to update.
        todo (TodoRequest): The request object containing updated todo details.

    Returns:
        Todos: The updated todo item, or None if not found.
    """
    db_todo = db.query(Todos).filter(Todos.id == id).first()
    if db_todo is None:
        return None
    db.query(Todos).filter(Todos.id == id).update({'description': todo.description, 'complete': todo.complete})
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, id: int):
    """
    Delete a todo item from the database.

    Args:
        db (Session): The database session.
        id (int): The ID of the todo item to delete.

    Returns:
        bool: True if the todo item was deleted, or None if not found.
    """
    todo = db.query(Todos).filter(Todos.id == id).first()
    if todo is None:
        return None
    db.query(Todos).filter(Todos.id == id).delete()
    db.commit()
    return True