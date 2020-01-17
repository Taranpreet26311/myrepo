from kafka import KafkaProducer
bootstrap_servers = ['localhost:9093']
topicName = 'test'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

ack =producer.send(topicName, b'Hello 9093!!!!!!!!')

metadata = ack.get()

print(metadata.topic)
print(metadata.partition)