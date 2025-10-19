from kafka import KafkaProducer
import json
from datetime import datetime
import time

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

# Sample air quality data
cities = ["Nairobi", "Mombasa"]
for city in cities:
    data = {
        "city": city,
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
        "carbon_monoxide": 0.3,
        "nitrogen_dioxide": 0.02,
        "ozone": 0.04,
        "pm10": 35.0,
        "pm25": 22.0,
        "sulphur_dioxide": 0.01,
        "uv_index": 5.0
    }

    producer.send("airqualitytopic", data)
    print(f"Inserted air quality data for {city}")
    time.sleep(1)

producer.flush()
