from beanie import Document
from pydantic import BaseModel, EmailStr, Field


class User(Document):
    username: str
    email: str
    password: str

    class Settings:
        name = "users"  # by default, if not having this settings, then the collection name is "Product"


class UserRequest(BaseModel):
    """
    # model for user signup
    """

    username: str
    email: str
    password: str

    class Settings:
        name = "users"  # by default, if not having this settings, then the collection name is "Product"
