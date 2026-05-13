from services.user_profile_service import calculate_risk_profile
from services.live_analytics_service import live_fund_analysis

from ai.huggingface_service import ask_huggingface

def personalized_reasoning_agent(
    age,
    income,
    goal,
    risk_appetite,
    scheme_code
):

    profile = calculate_risk_profile(
        age,
        income,
        goal,
        risk_appetite
    )

    analytics = live_fund_analysis(
        scheme_code
    )

    prompt = f"""
    Analyze this mutual fund investment opportunity.

    USER PROFILE:

    Age: {age}
    Income: {income}
    Goal: {goal}
    Risk Appetite: {risk_appetite}

    Calculated Risk Profile:
    {profile['risk_profile']}

    LIVE FUND ANALYTICS:

    Latest NAV:
    {analytics['latest_nav']}

    Volatility:
    {analytics['volatility']}%

    Provide:
    1. Personalized investment perspective
    2. Suitability analysis
    3. Risk considerations
    4. SIP strategy suggestion
    5. Long-term investment guidance

    Be practical and beginner friendly.
    """

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    return ask_huggingface(prompt)


if __name__ == "__main__":

    result = personalized_reasoning_agent(
        age=25,
        income=80000,
        goal="retirement",
        risk_appetite="moderate",
        scheme_code=119551
    )

    print(result)