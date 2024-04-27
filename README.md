```
# To-Do List API

This is a simple To-Do list API built using FastAPI framework with MongoDB Atlas as the database. It provides endpoints to perform CRUD operations on To-Do items.

## Installation

1. Clone the repository:
```

git clone <repository-url>

```

2. Install the dependencies:
```

pip install -r requirements.txt

```

## Configuration

Before running the API, make sure to set up the MongoDB Atlas connection URL, username, and password in the `config.py` file.

## Usage

1. Start the server:
```

uvicorn main:app --reload

```

2. Once the server is running, you can access the API documentation at `http://127.0.0.1:8000/docs`.

3. Use the API endpoints to manage your To-Do list:
   - `POST /todos/`: Create a new todo.
   - `GET /todos/{todo_id}`: Retrieve a todo by ID.
   - Implement other CRUD functionalities similarly.

```
