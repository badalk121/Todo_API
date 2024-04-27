"""
utils.py

Utility functions for the To-Do list API.
"""

from pymongo import MongoClient
from config import Settings

def get_db():
    """
    Function to get a connection to the MongoDB database.
    """
    client = MongoClient(Settings.mongodb_url)
    return client.todoapi
