from functools import lru_cache

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Base

from routers import todos

import config
from database import engine

# Create an instance of the FastAPI application
app = FastAPI()

# Include the todos router in the application
app.include_router(todos.router)

# Create all database tables defined in the Base metadata
Base.metadata.create_all(bind=engine)

# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,  # Allow credentials
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    """
    Handle HTTP exceptions and return a plain text response.

    Args:
        request: The request object.
        exc: The exception object.

    Returns:
        PlainTextResponse: A plain text response with the exception detail and status code.
    """
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@lru_cache()
def get_settings():
    """
    Get the application settings with caching.

    Returns:
        config.Settings: The application settings.
    """
    return config.Settings()