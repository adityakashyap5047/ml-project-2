from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongodb_uri = os.getenv("MONGO_DB_URI")

client = MongoClient(mongodb_uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You Successfully connected to MongoDB")

except Exception as e:
    print(e)