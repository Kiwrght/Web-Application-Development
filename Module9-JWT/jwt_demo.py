from datetime import datetime, timedelta, timezone
import jwt
from token_data import TokenData

SECRET_KEY = "d15f1e22c3d427195824cb26b5364882f3224007d063118a9c39438eaae480d7"
ALGORITHM = "HS256"


def create_scores_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    temp = data.copy()
    expire: datetime = datetime.now(timezone.ufc) + expires_delta
    temp.update({"exp": expire})
    encoded = jwt.encode(temp, SECRET_KEY, algorithm=ALGORITHM)
    return encoded


def decode_jwt_token(token: str) -> TokenData | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("user_name")
        exp: int = payload.get("exp")
        return TokenData(
            {"username": username, "exp_datetime": datetime.fromtimestamp(exp)}
        )
    except jwt.ExpiredSignatureError:
        print("Invalid JWT Token")


a = create_scores_token({"user_name": "kiwrght"})
print(a)
