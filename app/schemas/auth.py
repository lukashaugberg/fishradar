from pydantic import BaseModel, EmailStr


class RegisterIn(BaseModel):
    email: EmailStr
    username: str
    password: str
    first_name: str
    last_name: str


class LoginIn(BaseModel):
    email: EmailStr
    password: str


class TokenOut(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str
