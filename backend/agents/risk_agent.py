from services.fund_analytics_service import analyze_fund

# WHAT THIS DOES
# Risk Agent specializes ONLY in:
# volatility,
# drawdown,
# risk classification.

def risk_agent(scheme_code):

    analytics = analyze_fund(scheme_code)

    volatility = analytics["volatility"]
    drawdown = analytics["max_drawdown"]

    if volatility < 5:
        risk_level = "Low Risk"

    elif volatility < 15:
        risk_level = "Moderate Risk"

    else:
        risk_level = "High Risk"

    return {
        "scheme_code": scheme_code,
        "risk_level": risk_level,
        "volatility": volatility,
        "drawdown": drawdown
    }

if __name__ == "__main__":

    result = risk_agent(119551)

    print(result)