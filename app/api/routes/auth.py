from fastapi import APIRouter, Request, HTTPException, status

from app.schemas.auth import UserOut, RegisterIn
from app.services.user_service import UserService
from app.db.models import User

router = APIRouter()


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterIn, request: Request) -> User:
    db = request.state.db  # <- from middleware
    # Handles validation and creation via UserRepository as well (commit
    # happens in middleware)
    try:
        user = UserService.register_user(
            db,
            email=payload.email,
            username=payload.username,
            password=payload.password,
            first_name=payload.first_name,
            last_name=payload.last_name
        )
        return user
    except HTTPException as exc:
        raise exc
