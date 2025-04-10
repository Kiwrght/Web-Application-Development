from passlib.context import CryptContext

pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashPassword:
    def create_hash(self, passworrd: str) -> str:
        return pwd_content.hash(passworrd)
