from typing import List, Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from service import crud, db
from schemas import TodoRequest, TodoResponse

# Create a new APIRouter instance with a prefix for all routes
router = APIRouter(
    prefix="/todos"
)

# Annotated type for the database dependency
db_dependency = Annotated[Session, Depends(db.get_db)]

@router.post("", status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoRequest, db: db_dependency):
    """
    Create a new todo item.

    Args:
        todo (TodoRequest): The todo item to create.
        db (Session): The database session.

    Returns:
        TodoResponse: The created todo item.
    """
    todo = crud.create_todo(db, todo)
    return todo

@router.get("", response_model=List[TodoResponse])
def get_todos(db: db_dependency, completed: bool = None):
    """
    Retrieve a list of todo items.

    Args:
        db (Session): The database session.
        completed (bool, optional): Filter by completion status. Defaults to None.

    Returns:
        List[TodoResponse]: A list of todo items.
    """
    todos = crud.read_todos(db, completed)
    return todos

@router.put("/{id}")
def update_todo(db: db_dependency, id: int, todo: TodoRequest):
    """
    Update an existing todo item.

    Args:
        db (Session): The database session.
        id (int): The ID of the todo item to update.
        todo (TodoRequest): The updated todo item data.

    Raises:
        HTTPException: If the todo item is not found.

    Returns:
        TodoResponse: The updated todo item.
    """
    todo = crud.update_todo(db, id, todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="To Do item not found")
    return todo

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_todo(db: db_dependency, id: int):
    """
    Delete a todo item.

    Args:
        db (Session): The database session.
        id (int): The ID of the todo item to delete.

    Raises:
        HTTPException: If the todo item is not found.

    Returns:
        dict: A dictionary with a success message.
    """
    res = crud.delete_todo(db, id)
    if res is None:
        raise HTTPException(status_code=404, detail="To Do item not found")
    return res