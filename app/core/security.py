from passlib.context import CryptContext
from jose import jwt
import datetime

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd.verify(password, hashed)


def create_jwt(sub: str, secret: str, minutes: int) -> str:
    now = datetime.datetime.now()
    payload = {"sub": sub, "iat": now, "exp": now + datetime.timedelta(minutes=minutes)}
    return jwt.encode(payload, secret, algorithm="HS256")


def decode_jwt(token: str, secret: str) -> dict:
    return jwt.decode(token, secret, algorithms=["HS256"])
 