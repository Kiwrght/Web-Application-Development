app = FastAPI()


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> str:
    ##
    username = form_data.username
    return create_access_token({"username": username})


@app.get("/users/me")
async def read_my_username() -> TokenData:
    token = ""
    user = decode_jwt_token(token)
    return user
