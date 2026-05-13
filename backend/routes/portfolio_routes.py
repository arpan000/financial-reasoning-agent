from fastapi import APIRouter
from pydantic import BaseModel

from agents.portfolio_reasoning_agent import (
    portfolio_reasoning_agent
)

router = APIRouter()

class PortfolioRequest(BaseModel):

    age: int

    investment_horizon: int

    risk_appetite: str

    investment_amount: int

    goal: str

@router.post("/portfolio-advice")
def portfolio_advice(
    request: PortfolioRequest
):

    result = portfolio_reasoning_agent(

        age=request.age,

        investment_horizon=request.investment_horizon,

        risk_appetite=request.risk_appetite,

        investment_amount=request.investment_amount,

        goal=request.goal
    )

    return {
        "portfolio_advice": result
    }