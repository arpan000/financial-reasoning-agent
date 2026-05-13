from fastapi import APIRouter
from pydantic import BaseModel

from agents.coordinator_agent import coordinator_agent

router = APIRouter()

class UserProfile(BaseModel):

    age: int
    income: int
    goal: str
    risk_appetite: str
    scheme_code: int

@router.post("/agent-advisor")
def agent_advisor(profile: UserProfile):

    result = coordinator_agent(
        profile.dict(),
        profile.scheme_code
    )

    return result