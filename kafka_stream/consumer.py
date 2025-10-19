from kafka import KafkaConsumer
from cassandra.cluster import Cluster
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Connect to Cassandra
try:
    cluster = Cluster(['127.0.0.1'], protocol_version=5)
    session = cluster.connect()
    session.set_keyspace('air_quality')
    logging.info("✅ Connected to Cassandra successfully")
except Exception as e:
    logging.error(f"❌ Failed to connect to Cassandra: {e}")
    exit()

# Connect to Kafka
consumer = KafkaConsumer(
    'airqualitytopic',  # ✅ Make sure this matches your producer
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='air_quality_group',
    auto_offset_reset='earliest'
)

logging.info("✅ Kafka consumer is running and listening for messages...")

# Consume and insert into Cassandra
for message in consumer:
    try:
        data = message.value
        logging.info(f"📥 Received message for city: {data['city']}")

        session.execute("""
            INSERT INTO measurements (
                city, timestamp, carbon_monoxide, nitrogen_dioxide, ozone,
                pm10, pm25, sulphur_dioxide, uv_index
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data['city'],
            data['timestamp'],
            data['carbon_monoxide'],
            data['nitrogen_dioxide'],
            data['ozone'],
            data['pm10'],
            data['pm25'],
            data['sulphur_dioxide'],
            data['uv_index']
        ))

        logging.info(f"✅ Inserted data for {data['city']} at {data['timestamp']}")
    except Exception as e:
        logging.error(f"❌ Failed to process message: {e}")
