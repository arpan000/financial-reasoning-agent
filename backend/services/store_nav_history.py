from sqlalchemy import text
from database.db import engine
from api_integrations.mfapi_service import fetch_fund_details
from datetime import datetime

def store_nav_history(scheme_code):

    data = fetch_fund_details(scheme_code)

    nav_records = data.get("data", [])

    with engine.connect() as connection:

        for record in nav_records:

            try:
                nav_date = datetime.strptime(
                    record["date"],
                    "%d-%m-%Y"
                ).date()

                query = text("""
                    INSERT INTO nav_history
                    (scheme_code, nav_date, nav_value)
                    VALUES (:scheme_code, :nav_date, :nav_value)
                """)

                connection.execute(query, {
                    "scheme_code": scheme_code,
                    "nav_date": nav_date,
                    "nav_value": float(record["nav"])
                })

            except Exception as e:
                print(e)

        connection.commit()

    print("NAV history stored successfully")

if __name__ == "__main__":
    store_nav_history(119551)