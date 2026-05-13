from agents.risk_agent import risk_agent
from agents.recommendation_agent import recommendation_agent

def coordinator_agent(user_profile, scheme_code):

    risk_result = risk_agent(scheme_code)

    recommendation_result = recommendation_agent(user_profile)

    final_response = {
        "risk_analysis": risk_result,
        "recommendation": recommendation_result
    }

    return final_response

if __name__ == "__main__":

    profile = {
        "age": 24,
        "income": 50000,
        "goal": "wealth creation",
        "risk_appetite": "moderate"
    }

    result = coordinator_agent(
        profile,
        119551
    )

    print(result)