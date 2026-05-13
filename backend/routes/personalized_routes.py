from fastapi import APIRouter
from pydantic import BaseModel

from agents.personalized_reasoning_agent import (
    personalized_reasoning_agent
)

router = APIRouter()

class PersonalizedRequest(BaseModel):

    age: int
    income: int
    goal: str
    risk_appetite: str
    scheme_code: int

@router.post("/personalized-advice")
def personalized_advice(
    request: PersonalizedRequest
):

    result = personalized_reasoning_agent(
        age=request.age,
        income=request.income,
        goal=request.goal,
        risk_appetite=request.risk_appetite,
        scheme_code=request.scheme_code
    )

    return {
        "advice": result
    }