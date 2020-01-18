from kafka import KafkaProducer
bootstrap_servers = ['localhost:9093']
topicName = 'test2'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

ack =producer.send(topicName, b'Hello topic2 !!!!!!!!')

metadata = ack.get()

print(metadata.topic)
print(metadata.partition)