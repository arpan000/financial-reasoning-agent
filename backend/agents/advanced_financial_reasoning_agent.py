from services.financial_forecast_service import (
    calculate_sip_future_value,
    inflation_adjusted_value
)
print("Agent Started")
from services.portfolio_allocation_service import (
    generate_portfolio_allocation
)

from ai.huggingface_service import (
    ask_huggingface
)


def advanced_financial_reasoning_agent(

    name,

    age,

    monthly_income,

    investment_ratio,

    investment_years,

    risk_profile
):

    # Monthly Investment Calculation
    monthly_investment = (
        monthly_income
        * investment_ratio
    )

    # Expected CAGR Logic
    if risk_profile == "aggressive":

        expected_return = 14

    elif risk_profile == "moderate":

        expected_return = 11

    else:

        expected_return = 8

    # Future Corpus Forecast
    future_corpus = calculate_sip_future_value(

        monthly_investment=monthly_investment,

        annual_return=expected_return,

        years=investment_years
    )

    # Inflation Adjusted Corpus
    inflation_adjusted = inflation_adjusted_value(

        future_corpus,

        6,

        investment_years
    )

    # Portfolio Allocation
    allocation = generate_portfolio_allocation(
        risk_profile
    )

    # AI Reasoning Prompt
    prompt = f"""

    User Financial Profile:

    Name: {name}

    Age: {age}

    Monthly Income: ₹{monthly_income}

    Investment Ratio: {investment_ratio * 100}%

    Investment Years: {investment_years}

    Risk Profile: {risk_profile}

    Monthly Investment:
    ₹{monthly_investment}

    Expected CAGR:
    {expected_return}%

    Estimated Future Corpus:
    ₹{future_corpus}

    Inflation Adjusted Value:
    ₹{inflation_adjusted}

    Portfolio Allocation:
    {allocation}

    Provide:
    - personalized financial reasoning
    - portfolio explanation
    - long-term investment strategy
    - wealth creation guidance
    - risk analysis

    """

    response = ask_huggingface(
        prompt
    )

    return response


if __name__ == "__main__":

    result = advanced_financial_reasoning_agent(

        name="Ram",

        age=25,

        monthly_income=150000,

        investment_ratio=0.4,

        investment_years=7,

        risk_profile="aggressive"
    )

    print(result)