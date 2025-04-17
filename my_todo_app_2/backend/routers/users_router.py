from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from auth.jwt_auth import Token, TokenData, create_access_token, decode_jwt_token
from backend.models.users_model import User, UserRequest

pwd_context = CryptContext(schemes=["bcrypt"])


class HashPassword:
    def create_hash(self, password: str):
        return pwd_context.hash(password)

    def verify_hash(self, input_password: str, hashed_password: str):
        return pwd_context.verify(input_password, hashed_password)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
hash_password = HashPassword()


def get_user(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
    print(token)
    return decode_jwt_token(token)


user_router = APIRouter()


##ensure the username as certain length and not empty and password contains characters and length and numbers
##this demo is super simple
@user_router.post("/signup")
async def sign_up(user: UserRequest):
    ## Check if the user already exists in DB
    existing_user = await User.find_one(User.username == user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    ## Create a new user and save it to DB
    hashed_pwd = hash_password.create_hash(user.password)
    new_user = User(username=user.username, password=hashed_pwd, email=user.email)
    await new_user.insert_one()
    return {"message": "User created successfully"}


@user_router.post("/sign-in")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    ## Authenticate user by verifying the user in DB
    username = form_data.username
    existing_user = await User.find_one(User.username == username)
    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    authenticated = hash_password.verify_hash(
        form_data.password, existing_user.password
    )
    ## If the user is authenticated, create a JWT token and return it
    if authenticated:
        access_token = create_access_token({"username": username})
        return Token(access_token=access_token)

    return HTTPException(status_code=401, detail="Invalid username or password")
