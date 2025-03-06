
from fastapi import APIRouter
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

todo_router = APIRouter()

todo_list =[]

@todo_router.get("")
async def get_todos() -> dict:
    return {"todo": todo_list}


@todo_router.post("") # dont need the /todos because of the prefix in the include_router in main.py
async def add_todo(todo: Todo)-> dict:
    todo_list.append(todo)
    return{"msg": "new todo added"}
