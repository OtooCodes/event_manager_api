from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to Mongo Client cluster
mongo_client = MongoClient(os.getenv("MONGO_URI"))

# Access Database
event_manager_db = mongo_client["event_manager_db"]

# Pick a collection to operate on
event_collection = event_manager_db["events"]