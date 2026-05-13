from sqlalchemy import text
from database.db import engine
from api_integrations.mfapi_service import fetch_all_funds

def store_funds():
    funds = fetch_all_funds()

    with engine.connect() as connection:

        for fund in funds:
            try:
                query = text("""
                    INSERT IGNORE INTO mutual_funds
                    (scheme_code, scheme_name)
                    VALUES (:scheme_code, :scheme_name)
                """)

                connection.execute(query, {
                    "scheme_code": fund["schemeCode"],
                    "scheme_name": fund["schemeName"]
                })

            except Exception as e:
                print(e)

        connection.commit()

    print("Funds stored successfully")

if __name__ == "__main__":
    store_funds()