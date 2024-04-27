"""
models.py

Data models for the To-Do list API.
"""

from pydantic import BaseModel

class Todo(BaseModel):
    """
    Data model for a Todo item.
    """
    id: str = None
    title: str
    description: str
