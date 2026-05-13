from services.fund_comparison_service import (
    compare_funds
)

from ai.huggingface_service import ask_huggingface

def fund_recommendation_agent(
    investment_goal,
    risk_profile,
    category_keyword
):

    comparison = compare_funds(
        category_keyword
    )

    prompt = f"""
    You are a financial reasoning AI.

    USER PROFILE:

    Goal:
    {investment_goal}

    Risk Profile:
    {risk_profile}

    FUND ANALYTICS:

    {comparison}

    Analyze these funds and provide:

    1. Best suitable funds
    2. Risk comparison
    3. Diversification suggestions
    4. Long-term perspective
    5. SIP suitability

    Keep response beginner friendly.
    """

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    # return ask_huggingface(messages)
    return ask_huggingface(prompt)


if __name__ == "__main__":

    result = fund_recommendation_agent(
        investment_goal="retirement",
        risk_profile="moderate",
        category_keyword="small cap"
    )

    print(result)