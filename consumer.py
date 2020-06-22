from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'surprise_me',
     bootstrap_servers=['localhost:9092'])

for message in consumer:
    num = int(message.value.decode())
    if num % 2 == 1:
        print(f'Odd number {num} added to numtest. The whole message is {message}')