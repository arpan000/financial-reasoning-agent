from fastapi import APIRouter
from pydantic import BaseModel

from agents.conversational_financial_agent import (
    conversational_financial_agent
)

router = APIRouter()

class ConversationRequest(BaseModel):

    session_id: str

    message: str

@router.post("/financial-chat")
def financial_chat(
    request: ConversationRequest
):

    response = conversational_financial_agent(

        request.session_id,

        request.message
    )

    return {
        "response": response
    }