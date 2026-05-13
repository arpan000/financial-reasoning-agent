import numpy as np


# ----- CAGR (Compound Annual Growth Rate) Calculation ---------
def calculate_cagr(initial_value, final_value, years):

    cagr = ((final_value / initial_value) ** (1 / years)) - 1

    return round(cagr * 100, 2)

# Volatitlity Calculation ---------
def calculate_volatility(nav_values):

    returns = np.diff(nav_values) / nav_values[:-1]

    volatility = np.std(returns)

    return round(volatility * 100, 2) 

# sharpe_ratio = (mean_return - risk_free_rate) / volatility ----
def calculate_sharpe_ratio(avg_return, risk_free_rate, volatility):

    sharpe = (avg_return - risk_free_rate) / volatility

    return round(sharpe, 2)

# Drawdown Calculation ---------
def calculate_max_drawdown(nav_values):

    peak = nav_values[0]
    max_drawdown = 0

    for value in nav_values:

        if value > peak:
            peak = value

        drawdown = (peak - value) / peak

        if drawdown > max_drawdown:
            max_drawdown = drawdown

    return round(max_drawdown * 100, 2)

if __name__ == "__main__":

    result = calculate_cagr(
        initial_value=10000,
        final_value=20000,
        years=5
    )
    print("CAGR:", result, "%")

    sample_nav = [100, 102, 101, 105, 110, 108]
    volatility = calculate_volatility(sample_nav)
    print("Volatility:", volatility, "%")

    drawdown = calculate_max_drawdown(sample_nav)
    print("Max Drawdown:", drawdown, "%")