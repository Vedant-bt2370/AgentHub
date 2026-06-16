from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies.db import get_db
from dependencies.auth import get_current_user

from schemas.chat_schema import (
    ChatRequest,
    ChatResponse
)

from services.llm_service import (
    generate_response
)

from services.chat_service import (
    save_chat
)

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
        request: ChatRequest,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):

    answer = generate_response(
        request.question
    )

    save_chat(
        db,
        current_user.id,
        request.question,
        answer
    )

    return ChatResponse(
        answer=answer
    )