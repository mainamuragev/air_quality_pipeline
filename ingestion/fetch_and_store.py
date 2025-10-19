import requests, pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["air_quality"]
collection = db["measurements"]

def fetch(city, lat, lon):
    url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}"
    data = requests.get(url).json()
    record = {
        "city": city,
        "timestamp": datetime.utcnow(),
        "data": data.get("hourly", {})
    }
    collection.insert_one(record)
    print(f"Inserted air quality data for {city}")

fetch("Nairobi", -1.286389, 36.817223)
fetch("Mombasa", -4.043477, 39.668206)
