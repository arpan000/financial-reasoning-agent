from fastapi import APIRouter
from services.fund_analytics_service import analyze_fund

router = APIRouter()

@router.get("/analytics/{scheme_code}")
def fund_analytics(scheme_code: int):

    return analyze_fund(scheme_code)