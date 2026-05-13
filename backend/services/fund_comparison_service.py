from services.live_analytics_service import (
    live_fund_analysis
)

from services.fund_discovery_service import (
    search_funds
)

def compare_funds(keyword):

    funds = search_funds(keyword)

    comparison_results = []

    for fund in funds[:5]:

        try:

            analytics = live_fund_analysis(
                fund["scheme_code"]
            )

            comparison_results.append({

                "scheme_name": fund["scheme_name"],

                "scheme_code": fund["scheme_code"],

                "latest_nav": analytics["latest_nav"],

                "volatility": analytics["volatility"]
            })

        except Exception:

            continue

    sorted_results = sorted(
        comparison_results,
        key=lambda x: x["volatility"]
    )

    return sorted_results


if __name__ == "__main__":

    results = compare_funds("small cap")

    for item in results:

        print(item)