from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.user_schema import UserCreate
from dependencies import get_db
from services.auth_service import register_user

router = APIRouter()

@router.post("/register")
def register(
    request: UserCreate,
    db: Session = Depends(get_db)
):
    return register_user(
        db,
        request.email,
        request.password
    )