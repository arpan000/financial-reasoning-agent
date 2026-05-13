import requests

BASE_URL = "https://api.mfapi.in/mf"

def fetch_all_funds():

    response = requests.get(BASE_URL)

    data = response.json()

    return data

def search_funds(keyword):

    funds = fetch_all_funds()

    matched_funds = []

    keyword = keyword.lower()

    for fund in funds:

        scheme_name = fund["schemeName"].lower()

        if keyword in scheme_name:

            matched_funds.append({
                "scheme_code": fund["schemeCode"],
                "scheme_name": fund["schemeName"]
            })

    return matched_funds[:10]


if __name__ == "__main__":

    results = search_funds("small cap")

    for fund in results:

        print(fund)