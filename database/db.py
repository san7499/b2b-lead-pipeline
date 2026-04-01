from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["b2b_db"]
collection = db["companies"]

def insert_data():
    with open("data/cleaned.json") as f:
        data = json.load(f)

    collection.delete_many({})
    collection.insert_many(data)