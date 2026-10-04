from kafka import KafkaProducer
import json 
# from scripts.extract import get_weather
# from scripts.transform import transform_weather

def get_producer():
    return KafkaProducer(
        bootstrap_servers = 'localhost:9092',
        value_serializer = lambda value: json.dumps(value).encode("utf-8")  
    )


producer = get_producer()
producer.send(
    "weather",
    {"message": "Hello Kafka!"}
)

producer.flush()

print("message sent successfully")


# producer = KafkaProducer(
#     bootstrap_servers = 'localhost:9092',
#     value_serializer = lambda value: json.dumps(value).encode("utf-8")
# )

#tells the producer to send a message to kafka topic. producer(topic, message)
# producer.send(
#     "weather",
#     {"message": "Hello Kafka!"}
#     )

# extracted_weather = get_weather(-1.2833, 36.8167)
# transformed_weather = transform_weather(extracted_weather)
# producer.send(
#     "weather",
#     transformed_weather
#     )




#send everything thats currently in the buffer before closing 
# producer.flush() 


# print("message sent successfully")



