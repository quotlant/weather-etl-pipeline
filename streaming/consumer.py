from kafka import KafkaConsumer
import json
from scripts.load import load_weather


consumer = KafkaConsumer(
    "weather",
    bootstrap_servers = "localhost:9092",
    group_id = "weather-consumer-group"

    
)

#The replay consumer group is only useful for reprocessing all historical messages that i accidentally deleted from my weather table.
consumer = KafkaConsumer(
    "weather",
    bootstrap_servers="localhost:9092",
    group_id="weather-consumer-group-replay",
    auto_offset_reset="earliest",
)

for message in consumer:
    data = json.loads(message.value.decode("utf-8"))
    print(data)
    load_weather(data)