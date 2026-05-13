# phase 1: Initial Setup and Basic API
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Financial Reasoning Agent Running Successfully"}

# phase 2: Database Integration
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.funds import router as funds_router
from routes.analytics import router as analytics_router
from routes.chat import router as chat_router
from routes.rag_chat import router as rag_router
from routes.agent_routes import router as agent_router
from routes.personalized_routes import (
    router as personalized_router
)
from routes.fund_recommendation_routes import (
    router as recommendation_router
)
from routes.portfolio_routes import (
    router as portfolio_router
)
from routes.conversation_routes import (
    router as conversation_router
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(funds_router)
app.include_router(analytics_router)
app.include_router(chat_router)
app.include_router(rag_router)
app.include_router(agent_router)
app.include_router(personalized_router)
app.include_router(recommendation_router)
app.include_router(portfolio_router)
app.include_router(conversation_router)

@app.get("/")
def home():
    return {
        "message": "Financial Reasoning Agent Running Successfully"
    }

# phase 3: API Integrations and Analytics