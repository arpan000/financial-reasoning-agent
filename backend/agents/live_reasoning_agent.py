from services.live_analytics_service import live_fund_analysis
from ai.huggingface_service import ask_huggingface

def live_reasoning_agent(scheme_code):

    analytics = live_fund_analysis(scheme_code)

    prompt = f"""
    Analyze this mutual fund using LIVE market data.

    Scheme Code: {scheme_code}

    Latest NAV: {analytics['latest_nav']}

    Volatility: {analytics['volatility']}%

    Explain:
    - current risk level
    - suitability
    - investment perspective
    - long-term outlook

    Keep explanation beginner friendly.
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

    result = live_reasoning_agent(119551)

    print(result)