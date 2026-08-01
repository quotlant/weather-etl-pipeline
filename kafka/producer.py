from kafka import KafkaProducer
import json 

producer = KafkaProducer(
    bootstrap_servers = 'localhost:9092',
    value_serializer = lambda value: json.dumps(value).encode("utf-8")
)

#tells the producer to send a message to kafka topic. producer(topic, message)
producer.send(
    "weather",
    {"message": "Hello Kafka!"}
    )

#send everything thats currently in the buffer before closing 
producer.flush() 


print("message sent successfully")



