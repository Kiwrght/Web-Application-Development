from beanie import Document
from pydantic import BaseModel, Field


class Movie(Document):
    title: str
    year: int

    class Settings:
        collection = "movies"


class MovieRequest(BaseModel):
    title: str
    year: int
