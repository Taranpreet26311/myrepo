from kafka import KafkaConsumer
import sys
topicName = 'test2'
consumer = KafkaConsumer(topicName,
                     bootstrap_servers=['localhost:9092'],
                     group_id=None,
                     auto_offset_reset='earliest')

print ("Consuming messages from the given topic")
for message in consumer:
    print ("Message"), message
    if message is not None:
        print (message.offset)
        print(message.value)

print ("Quit")