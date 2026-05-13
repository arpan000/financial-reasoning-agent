from sqlalchemy import text
from database.db import engine

def get_nav_history(scheme_code):

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT nav_value
                FROM nav_history
                WHERE scheme_code = :scheme_code
                ORDER BY nav_date
            """),
            {"scheme_code": scheme_code}
        )

        nav_values = [float(row[0]) for row in result]

    return nav_values

from analytics.financial_metrics import (
    calculate_volatility,
    calculate_max_drawdown
)

#  combine Analytics functions to analyze a fund's performance based on its NAV history
def analyze_fund(scheme_code):

    nav_values = get_nav_history(scheme_code)

    if len(nav_values) < 2:
        return {"error": "Not enough data"}

    volatility = calculate_volatility(nav_values)

    drawdown = calculate_max_drawdown(nav_values)

    return {
        "scheme_code": scheme_code,
        "volatility": volatility,
        "max_drawdown": drawdown
    }

# Test anaysis service
if __name__ == "__main__":

    result = analyze_fund(119551)

    print(result)