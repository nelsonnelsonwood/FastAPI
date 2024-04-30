from fastapi import FastAPI
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

# Example
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None