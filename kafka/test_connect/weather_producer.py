from kafka import KafkaProducer
import requests
import json
import time

# Kafka configuration
KAFKA_BROKER = 'localhost:9092'
TOPIC = 'weather_data'

# OpenWeather API configuration
API_KEY = '06114e975d192382ea2a54158e5b1ee6'
CITY = 'Hanoi'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def fetch_weather_data():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == '__main__':
    while True:
        weather_data = fetch_weather_data()
        if weather_data:
            producer.send(TOPIC, weather_data)
            print(f"Sent data: {weather_data}")
        time.sleep(60)  # Fetch data every 60 seconds
