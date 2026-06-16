from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies.db import get_db
from core.oauth import oauth2_scheme
from core.security import decode_access_token
from services.user_service import get_user_by_email


def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):

    email = decode_access_token(token)

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = get_user_by_email(
        db,
        email
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user