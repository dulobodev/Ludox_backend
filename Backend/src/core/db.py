from pymongo import MongoClient

import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

client = MongoClient(f"mongodb+srv://{DB_NAME}:{DB_PASSWORD}@ludox.6bhfhml.mongodb.net/?retryWrites=true&w=majority&appName=Ludox")