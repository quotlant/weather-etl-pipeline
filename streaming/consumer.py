from kafka import KafkaConsumer
import json
from scripts.load import load_weather


consumer = KafkaConsumer(
    "weather",
    bootstrap_servers = "localhost:9092",
    group_id = "weather-consumer-group"

    
)

for message in consumer:
    data = json.loads(message.value.decode("utf-8"))
    print(data)
    load_weather(data)