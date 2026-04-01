from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["b2b_db"]
collection = db["companies"]


def insert_data():
    try:
        with open("data/cleaned.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print("❌ Error loading cleaned data:", e)
        return

    if not data:
        print("⚠️ No data to insert.")
        return

    try:
        collection.delete_many({})
        collection.insert_many(data)
        print(f"✅ Inserted {len(data)} records into MongoDB")
    except Exception as e:
        print("❌ DB Error:", e)


if __name__ == "__main__":
    insert_data()