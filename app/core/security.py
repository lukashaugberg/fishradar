from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import jwt, JWTError

from app.core.config import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(subject: str, expires_minutes: int | None = None) -> str:
    now = datetime.now()
    exp_minutes = expires_minutes or config.jwt_acess_token_exp_minutes

    payload = {
        "sub": subject,
        "iat": now,
        "exp": now + timedelta(minutes=exp_minutes)
    }

    secret = config.jwt_secret_key.get_secret_value()
    return jwt.encode(payload, secret, algorithm=config.jwt_algorithm)


def decode_jwt(token: str) -> dict:
    secret = config.jwt_secret_key.get_secret_value()
    try:
        return jwt.decode(token, secret, algorithms=[config.jwt_algorithm])
    except JWTError as exc:
        raise ValueError("Invalid token") from exc
