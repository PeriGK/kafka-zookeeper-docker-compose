from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group')

for message in consumer:
    print('{} added to {}'.format(message, collection))