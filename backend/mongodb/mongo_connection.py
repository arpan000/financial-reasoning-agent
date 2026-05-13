from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"

client = MongoClient(MONGO_URI)

db = client["financial_reasoning_ai"]

conversation_collection = db["conversations"]

print("MongoDB Connected Successfully")