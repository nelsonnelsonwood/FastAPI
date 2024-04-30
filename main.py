# Fast API, it also support http basic OAuth2 tokens (jwt tokens) and hear API keys. Not in this demo.
print("+---------------------------------------------------------------------------------+")
print("| Fast API Demo by Nelson A. Nelson nelsonnelso@hotmail.com @AstorSkywalker 2023  |")
print("| To run the server in a terminal type: uvicorn main:app --reload                 |")
print("| To view swagger docs and redoc docs generated automatically by FasAPI go to:    |")
print("| http://localhost:8000/docs/                                                     |")
print("| http://localhost:8000/redoc/                                                    |")
print("+---------------------------------------------------------------------------------+")
print("https://youtu.be/cbASjoZZGIw?si=z9riKtzgyeJITMVG")

#from typing import Union
from fastapi import FastAPI
from models import Todo

app = FastAPI()

# This list will serve as a database
todos = []

@app.get("/")
async def read_root():
    return {"message": "Welcome to Nelson's World!"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# Get all TODOs
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get single TODOs
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No todo found with id: " + str(todo_id)}

# Create a TODO
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added"}

# Update a TODO:
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": "No todo found with id: " + str(todo_id) + " to update."}

# Delete a TODO:
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo id: " + str(todo_id) + " has been deleted."}
    return {"message": "No todo found with id: " + str(todo_id)}