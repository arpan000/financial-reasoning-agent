def calculate_risk_profile(age, income, goal, risk_appetite):

    score = 0

    # Age scoring
    if age < 30:
        score += 3

    elif age < 45:
        score += 2

    else:
        score += 1

    # Income scoring
    if income > 100000:
        score += 3

    elif income > 50000:
        score += 2

    else:
        score += 1

    # Goal scoring
    long_term_goals = [
        "retirement",
        "wealth creation",
        "long term"
    ]

    if goal.lower() in long_term_goals:
        score += 3

    else:
        score += 1

    # Risk appetite scoring
    if risk_appetite.lower() == "high":
        score += 3

    elif risk_appetite.lower() == "moderate":
        score += 2

    else:
        score += 1

    # Final classification
    if score >= 10:
        profile = "Aggressive"

    elif score >= 7:
        profile = "Moderate"

    else:
        profile = "Conservative"

    return {
        "risk_score": score,
        "risk_profile": profile
    }


if __name__ == "__main__":

    result = calculate_risk_profile(
        age=25,
        income=80000,
        goal="retirement",
        risk_appetite="moderate"
    )

    print(result)