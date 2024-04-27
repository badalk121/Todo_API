"""
main.py

This file contains the main FastAPI application for the To-Do list API.
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel
from config import Settings
from models import Todo
from utils import get_db

app = FastAPI()
security = HTTPBasic()

def get_db_client():
    """
    Function to get a connection to the MongoDB database.
    """
    return MongoClient(Settings.mongodb_url)

@app.post("/todos/", response_model=Todo)
async def create_todo(todo: Todo, credentials: HTTPBasicCredentials = Depends(security)):
    """
    Endpoint to create a new todo.
    """
    if not authenticate(credentials):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    db = get_db()
    result = db.todos.insert_one(todo.dict())
    todo.id = str(result.inserted_id)
    return todo

@app.get("/todos/{todo_id}", response_model=Todo)
async def read_todo(todo_id: str, credentials: HTTPBasicCredentials = Depends(security)):
    """
    Endpoint to retrieve a todo by ID.
    """
    if not authenticate(credentials):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    db = get_db()
    todo = db.todos.find_one({"_id": ObjectId(todo_id)})
    if todo:
        return Todo(**todo)
    raise HTTPException(status_code=404, detail="Todo not found")

def authenticate(credentials: HTTPBasicCredentials):
    """
    Function to authenticate user credentials.
    """
    correct_username = Settings.username
    correct_password = Settings.password
    return credentials.username == correct_username and credentials.password == correct_password
