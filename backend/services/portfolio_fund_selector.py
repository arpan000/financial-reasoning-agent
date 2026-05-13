from services.fund_discovery_service import (
    search_funds
)

def select_portfolio_funds(
    allocation
):

    selected_funds = {}

    for category in allocation:

        try:

            funds = search_funds(category)

            if funds:

                selected_funds[category] = {
                    "allocation_percent":
                    allocation[category],

                    "selected_fund":
                    funds[0]
                }

        except Exception:

            continue

    return selected_funds


if __name__ == "__main__":

    allocation = {

        "Large Cap": 40,

        "Flexi Cap": 30,

        "Mid Cap": 15,

        "Debt Fund": 15
    }

    result = select_portfolio_funds(
        allocation
    )

    print(result)