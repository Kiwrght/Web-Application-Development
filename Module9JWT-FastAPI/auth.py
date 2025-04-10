from datetime import datetime, timedelta, timezone
import jwt
from pydantic import BaseModel


class TokenData(BaseModel):
    username: str
    exp_datetime: datetime


SECRET_KEY = "2a33c01bffbd1620f710c408f0a630f839e449b4c3356a15866347f9416bdef5"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    payload.update({"exp": expire})
    encoded = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded


def decode_jwt_token(token: str) -> TokenData | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("user_name")
        exp: int = payload.get("exp")
        return TokenData(username=username, exp_datetime=datetime.fromtimestamp(exp))
    except jwt.InvalidTokenError:
        print("Invalid JWT token.")
