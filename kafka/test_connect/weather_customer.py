from kafka import KafkaConsumer
import json

# Kafka configuration
KAFKA_BROKER = 'localhost:9092'
TOPIC = 'weather_data'

# Initialize Kafka consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

if __name__ == '__main__':
    print("Listening for weather data...")
    for message in consumer:
        weather_data = message.value
        print(f"Received data: {weather_data}")
        # Process or store data as needed
