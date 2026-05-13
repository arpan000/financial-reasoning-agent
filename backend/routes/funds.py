from fastapi import APIRouter
from sqlalchemy import text
from database.db import engine

router = APIRouter()

@router.get("/funds")
def get_funds():

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT * FROM mutual_funds LIMIT 100")
        )

        funds = [dict(row._mapping) for row in result]

    return funds