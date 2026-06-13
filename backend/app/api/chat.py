from fastapi import APIRouter
from schemas.chat_schema import ChatRequest, ChatResponse
from services.llm_service import generate_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = generate_response(request.question)

    return ChatResponse(answer=answer)