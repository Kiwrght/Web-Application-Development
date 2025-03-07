from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    desc: str


class TodoRequest(BaseModel):
    title: str
    desc: str
