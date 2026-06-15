from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db

from schemas.user_schema import UserCreate
from schemas.auth_schema import LoginRequest, TokenResponse

from services.auth_service import (
    register_user,
    authenticate_user
)

from core.security import create_access_token

router = APIRouter()


@router.post("/register")
def register(
    request: UserCreate,
    db: Session = Depends(get_db)
):
    user = register_user(
        db,
        request.email,
        request.password
    )

    return {
        "id": user.id,
        "email": user.email
    }


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = authenticate_user(
        db,
        request.email,
        request.password
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }