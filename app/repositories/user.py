from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.models import User


class UserRepository:
    """
    ...
    """
    @staticmethod
    def get_by_email(db: Session, email: str) -> User | None:
        """
        ...
        """
        stmt = select(User).where(User.email == email)
        result = db.execute(stmt).scalar_one_or_none()

        return result


    @staticmethod
    def get_by_user_id(db: Session, user_id: int) -> User | None:
        """
        ...
        """
        stmt = select(User).where(User.id == user_id)
        result = db.execute(stmt).scalar_one_or_none()

        return result


    @staticmethod
    def create(
        db: Session,
        *,
        email: str,
        username: str,
        password_hash: str,
        first_name: str,
        last_name: str
    ) -> User:
        """
        ...
        """
        user = User(
            email=email,
            username=username,
            password_hash=password_hash,
            first_name=first_name,
            last_name=last_name
        )

        db.add(user)  # add to session
        db.flush()  # INSERT (user.id is available)
        db.refresh(user)  # gives 'user' all server-generated values (we do
                          # do this to be able to access these values without
                          # committing (committing happens in middleware))
        return user
