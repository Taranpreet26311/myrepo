from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='172.31.0.2:9092')
producer.send('sample', b'Hello, World!')
producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')