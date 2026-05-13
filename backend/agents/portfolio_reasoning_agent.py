from services.portfolio_optimizer import (
    generate_portfolio_allocation
)

from services.portfolio_fund_selector import (
    select_portfolio_funds
)

from ai.huggingface_service import (
    ask_huggingface
)

def portfolio_reasoning_agent(

    age,

    investment_horizon,

    risk_appetite,

    investment_amount,

    goal
):

    allocation = generate_portfolio_allocation(

        age,

        investment_horizon,

        risk_appetite
    )

    selected_funds = select_portfolio_funds(
        allocation
    )

    prompt = f"""
    You are an AI portfolio advisor.

    USER PROFILE:

    Age: {age}

    Investment Horizon:
    {investment_horizon} years

    Risk Appetite:
    {risk_appetite}

    Investment Amount:
    ₹{investment_amount}

    Goal:
    {goal}

    GENERATED PORTFOLIO:

    {selected_funds}

    Explain:

    1. Portfolio diversification
    2. Allocation reasoning
    3. Risk-return balance
    4. Long-term perspective
    5. SIP/STP suggestions

    Keep explanation beginner friendly.
    """

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    return ask_huggingface(prompt)


if __name__ == "__main__":

    result = portfolio_reasoning_agent(

        age=25,

        investment_horizon=15,

        risk_appetite="moderate",

        investment_amount=2000000,

        goal="retirement"
    )

    print(result)