from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI(title="Fruit Basket")  # Can get more details in the slides

# Description, summary and Documentation with in these assignments however for public use it is wise to use them


@app.get(
    "/items/{item_id}*",
    summary="Create an item",
    description="Create an item with all the information name, description, price, tax, and a set of unique tags",
)
async def get_item_by_id(
    item_id: Annotated[
        int,
        Path(
            title="This is the Item ID, which should be an integer.",
            ge=0,
            le=1000,
            multiple_of=3,
        ),
    ]
) -> dict:

    return {"item_id": item_id}
