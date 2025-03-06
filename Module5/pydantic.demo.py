from datetime import datetime
from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {
    "id": 123,
    "first_name": "Tom",  # if first_name is Name it will be introduced as a new Field
    "signup_ts": "2020-09-11 12:22",
    "tastes": {
        "wine": 9,
        "cabbage": "1",
    },  # using "-1" will cause an error due to package PositiveInt
}

user = User(**external_data)

print(user.tastes)
print(user.name)
# you can also try to put cabbage
