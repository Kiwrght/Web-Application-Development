from pydantic import BaseModel
from beanie import Document


## take out ID because it is automatically made in mongoDB
class Todo(Document):
    title: str
    description: str


class TodoRequest(BaseModel):
    title: str
    description: str
