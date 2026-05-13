from fastapi import APIRouter
from pydantic import BaseModel

from agents.fund_recommendation_agent import (
    fund_recommendation_agent
)

router = APIRouter()

class RecommendationRequest(BaseModel):

    investment_goal: str
    risk_profile: str
    category_keyword: str

@router.post("/fund-recommendation")
def fund_recommendation(
    request: RecommendationRequest
):

    result = fund_recommendation_agent(
        investment_goal=request.investment_goal,
        risk_profile=request.risk_profile,
        category_keyword=request.category_keyword
    )

    return {
        "recommendation": result
    }