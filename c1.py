from pykafka import KafkaClient

client = KafkaClient(hosts='127.0.0.1:9092')
topic = client.topics['digits']
consumer = topic.get_simple_consumer()

for i in consumer:
    print(i.offset, ' : ', i.value.decode('utf-8'))