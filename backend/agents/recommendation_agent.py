from ai.huggingface_service import ask_huggingface

def recommendation_agent(user_profile):

    prompt = f"""
    Suggest a mutual fund investment strategy.

    User Profile:
    {user_profile}

    Include:
    - risk level
    - investment approach
    - SIP strategy
    - diversification advice
    """

    return ask_huggingface(prompt)

if __name__ == "__main__":

    profile = {
        "age": 24,
        "income": 50000,
        "goal": "retirement",
        "risk_appetite": "moderate"
    }

    result = recommendation_agent(profile)

    print(result)