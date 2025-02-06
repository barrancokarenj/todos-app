from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):
    """
    SQLAlchemy model for the 'todos' table.

    Attributes:
        id (int): The primary key of the todo item.
        description (str): The description of the todo item.
        complete (bool): The completion status of the todo item.
    """
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    complete = Column(Boolean, default=False)
