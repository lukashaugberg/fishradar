from fastapi import APIRouter, Request, HTTPException

from app.schemas.auth import UserOut, RegisterIn
from app.services.user_service import UserService

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register(payload: RegisterIn, request: Request):
    db = request.state.db  # <- from middleware
    # Handles validation and creation via UserRepository as well (commit
    # happens in middleware)
    user = UserService.register_user(
        db,
        email=payload.email,
        username=payload.username,
        password=payload.password,
        first_name=payload.first_name,
        last_name=payload.last_name
    )
    return user
