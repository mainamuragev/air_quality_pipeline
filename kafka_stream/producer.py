from kafka import KafkaProducer
import json
import time
from datetime import datetime
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "location": "Nairobi",
        "timestamp": datetime.utcnow().isoformat(),
        "pm2_5": round(random.uniform(10, 100), 2),
        "pm10": round(random.uniform(20, 150), 2),
        "humidity": round(random.uniform(30, 90), 2)
    }
    producer.send('air_quality', value=data)
    print("Sent:", data)
    time.sleep(2)
