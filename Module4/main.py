from enum import Enum
from fastapi import FastAPI  # type: ignore
from todo import todo_router

app = FastAPI()
app.include_router(todo_router, tags=["todos"], prefix = "/todos")

@app.get("/")
async def welcome() -> dict:
    """My Document summary"""
    return {"msg": "Hello World!"}


# same route path will show the latest one
# route path example: /items or /
# use snake case naming convention
@app.get("/items")
async def get_items() -> dict:
    return {"item1": "book1"}


# works
@app.get("/items/foo")
async def get_items() -> dict:
    return {"foo": "bar"}


@app.get("/items/{id}")
async def get_items(id: int) -> dict:
    if id == 1:
        return {"item1": "book1"}
    else:
        return {}


@app.get("/items/r")  # this path doesn't work
async def get_items() -> dict:
    return {"foo": "bar"}


class PersonType(str, Enum):
    student = "Student"
    employee = "Employee"
    patient = "Patient"


# have to type exactly what is the in the Person type class
# can do class.enum to have  a drop down of available options
@app.get("/persons/{person_type}")
async def get_items(person_type: PersonType) -> dict:
    if person_type is PersonType.student:
        return {"item1": "book1"}
    if person_type is PersonType.employee:
        return {"employee1": "name name1", "employee2": "name name2"}
    if person_type.value == "Patient":
        return {"patient1": "p1 t1"}
    else:
        return {}
