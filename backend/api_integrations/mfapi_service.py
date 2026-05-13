import requests

BASE_URL = "https://api.mfapi.in/mf"

def fetch_all_funds():
    try:
        response = requests.get(BASE_URL)

        if response.status_code == 200:
            data = response.json()
            print(f"Total Funds Fetched: {len(data)}")

            # Print first 5 funds
            for fund in data[:5]:
                print(fund)

            return data

        else:
            print("Failed to fetch data")

    except Exception as e:
        print("Error:", e)

# if __name__ == "__main__":
#     fetch_all_funds()

def fetch_fund_details(scheme_code):
    try:
        url = f"{BASE_URL}/{scheme_code}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            print("Fund Name:", data.get("meta", {}).get("scheme_name"))

            # Print first 5 NAV records
            for nav in data.get("data", [])[:5]:
                print(nav)

            return data

        else:
            print("Failed to fetch fund details")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    fetch_fund_details(119551)