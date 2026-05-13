def generate_portfolio_allocation(
    age,
    investment_horizon,
    risk_appetite
):

    allocation = {}

    # AGGRESSIVE PROFILE
    if (
        risk_appetite.lower() == "high"
        and investment_horizon >= 10
    ):

        allocation = {

            "Large Cap": 35,

            "Flexi Cap": 25,

            "Mid Cap": 20,

            "Small Cap": 15,

            "Debt Fund": 5
        }

    # MODERATE PROFILE
    elif (
        risk_appetite.lower() == "moderate"
    ):

        allocation = {

            "Large Cap": 40,

            "Flexi Cap": 30,

            "Mid Cap": 15,

            "Debt Fund": 15
        }

    # CONSERVATIVE PROFILE
    else:

        allocation = {

            "Large Cap": 30,

            "Debt Fund": 50,

            "Hybrid Fund": 20
        }

    return allocation


if __name__ == "__main__":

    result = generate_portfolio_allocation(
        age=25,
        investment_horizon=15,
        risk_appetite="moderate"
    )

    print(result)