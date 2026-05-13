import requests

BASE_URL = "https://api.mfapi.in/mf"

def fetch_live_nav(scheme_code):

    try:

        url = f"{BASE_URL}/{scheme_code}"

        response = requests.get(url)

        data = response.json()

        latest_nav = data["data"][0]

        return {
            "scheme_name": data["meta"]["scheme_name"],
            "nav": latest_nav["nav"],
            "date": latest_nav["date"]
        }

    except Exception as e:

        return {
            "error": str(e)
        }


if __name__ == "__main__":

    result = fetch_live_nav(119551)

    print(result)