from fastapi import APIRouter
from pydantic import BaseModel

from rag.rag_pipeline import rag_financial_chat

router = APIRouter()

class RAGChatRequest(BaseModel):
    question: str

@router.post("/rag-chat")
def rag_chat(request: RAGChatRequest):

    answer = rag_financial_chat(request.question)

    return {
        "question": request.question,
        "answer": answer
    }