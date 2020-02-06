from pykafka import KafkaClient
import time

client = KafkaClient(hosts='127.0.0.1:9092')
topic = client.topics['digits']
producer = topic.get_sync_producer()

i = 1
while True:
    producer.produce(str(i).encode('utf-8'))
    i += 2
    time.sleep(2)
