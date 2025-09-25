from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "Url"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.mydatabase