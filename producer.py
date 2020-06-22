from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['130.61.225.214:9092'])

for e in range(1000):
    data = {'number' : e}
    producer.send('numtest', value=data)
    sleep(5)