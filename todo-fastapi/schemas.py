from pydantic import BaseModel, Field

class TodoRequest(BaseModel):
    """
    Schema for a request to create or update a Todo item.

    Attributes:
        description (str): The description of the Todo item.
        complete (bool): Indicates whether the Todo item is complete. Defaults to False.
    """
    description: str
    complete: bool = Field(default=False)

class TodoResponse(BaseModel):
    """
    Schema for a response containing a Todo item.

    Attributes:
        id (int): The unique identifier of the Todo item.
        description (str): The description of the Todo item.
        complete (bool): Indicates whether the Todo item is complete.
    """
    id: int
    description: str
    complete: bool

class Config:
    """
    Configuration for Pydantic models.

    Attributes:
        orm_mode (bool): Enables ORM mode which allows the model to be created from ORM objects.
    """
    orm_mode = True