import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.getenv("MONGO_URL")

client = AsyncIOMotorClient(MONGO_URL)
database = client["kyc_fraud_detection"]
logs_collection = database["logs"]

print("MONGO_URL =", MONGO_URL)
