from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.user import UserRepository
from app.core.security import hash_password
from app.db.models.user import User


class UserService:
    """
    """
    @staticmethod
    def register_user(
        db: Session,
        *,
        email: str,
        username: str,
        password: str,
        first_name: str,
        last_name: str
    ) -> User:
        """
        """
        existing = UserRepository.get_by_email(db, email)
        if existing:
            raise HTTPException(400, "Email already registered")

        hashed_password = hash_password(password)
        user = UserRepository.create(
            db,
            email=email,
            username=username,
            password_hash=hashed_password,
            first_name=first_name,
            last_name=last_name
        )

        return user
