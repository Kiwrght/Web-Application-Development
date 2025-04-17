from beanie import init_beanie
from models.my_config import get_settings
from motor.motor_asyncio import AsyncIOMotorClient

from models.todo_model import Todo
from models.users_model import User


async def init_database():
    my_config = get_settings()
    client = AsyncIOMotorClient(my_config.connection_string)
    db = client["todo_app"]
    await init_beanie(database=db, document_models=[User, Todo])
