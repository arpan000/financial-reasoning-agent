from fastapi import APIRouter
from pydantic import BaseModel
from ai.huggingface_service import ask_huggingface

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
def chat(request: ChatRequest):

    answer = ask_huggingface(request.question)

    return {
        "question": request.question,
        "answer": answer
    }