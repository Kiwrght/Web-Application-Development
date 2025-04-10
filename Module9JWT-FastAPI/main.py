from contextvars import Token
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from auth import TokenData, create_access_token, decode_jwt_token, authenticated
from hash_pass import HashPassword


in_memory_db = [
    {
        "username": "test",
        "password": "test",
    },
]
hash_password = HashPassword()

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
hash_password = 

def get_user(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
    print(token)
    return decode_jwt_token(token)


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    ## Authenticate User by verifying username in db
    username = form_data.username
    for u in in_memory_db:
        if u["username"] == username:
           hash_password.verify(u["password"], form_data.password)
           if authenticated:
               access_token = create_access_token(username, "username")
               return Token(access_token=access_token)

    raise HTTPException(
        status_code=401, detail="Incorrect username or password"
    ) # always use to deter hackers from knowing which is wrong


@app.get("/users/me")
async def read_my_username() -> TokenData:
    token = ""
    user = decode_jwt_token(token)
    return user
