from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from auth import TokenData, create_access_token, decode_jwt_token


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
    print(token)

    user = decode_jwt_token(token)
    if not user:
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials"
        )
    return user


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> str:
    ## assume user is authenticated by username and password verification
    username = form_data.username
    return create_access_token({"username": username})


@app.get("/users/me")
async def read_my_username() -> TokenData:
    token = ""
    user = decode_jwt_token(token)
    return user
