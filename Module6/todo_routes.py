from sys import prefix
from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, status
from todo import Todo

max_id: int = 0

todo_router = APIRouter(prefix="/todos")

todo_list = []


@todo_router.get("/")
async def get_todos() -> list:
    return {"todos": todo_list}


@todo_router.post("/add", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Todo) -> Todo:
    todo.list.append(todo)
    return todo


# Searching for ID
@todo_router.get("/{id}")
async def get_todo_by_id(id: Annotated[int, Path(ge=0, le=1000)]) -> Todo:
    global max_id  # Using the global variable
    max_id += 1  # Incrementing the ID by one
    newTodo = Todo(id=max_id, title=todo.title, desc=todo.desc)
    for todo in todo_list:
        if todo.id == id:
            return todo

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID= {id} is not found"
    )


# Deleting ID
@todo_router.delete("/{id}")
async def delete_todo_by_id(id: Annotated[int, Path(ge=0, le=1000)]) -> dict:
    for i in range(len(todo_list)):
        todo = todo_list[i]

        if todo.id == id:
            todo_list.pop(i)
            return {"msg": f"The todo with ID= {id} deleted successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID= {id} is not found"
    )
