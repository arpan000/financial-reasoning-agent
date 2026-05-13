import requests
import numpy as np

BASE_URL = "https://api.mfapi.in/mf"

def fetch_historical_navs(scheme_code):

    url = f"{BASE_URL}/{scheme_code}"

    response = requests.get(url)

    data = response.json()

    navs = []

    for item in data["data"][:90]:

        navs.append(float(item["nav"]))

    return navs

def calculate_live_volatility(navs):

    returns = []

    for i in range(1, len(navs)):

        daily_return = (
            (navs[i-1] - navs[i]) / navs[i]
        )

        returns.append(daily_return)

    volatility = np.std(returns) * 100

    return round(volatility, 2)

def live_fund_analysis(scheme_code):

    navs = fetch_historical_navs(scheme_code)

    volatility = calculate_live_volatility(navs)

    return {
        "scheme_code": scheme_code,
        "volatility": volatility,
        "latest_nav": navs[0]
    }


if __name__ == "__main__":

    result = live_fund_analysis(119551)

    print(result)