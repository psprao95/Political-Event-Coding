from kafka import KafkaConsumer
from json import loads
import csv
import re


file_name='data2.csv'
topic_name='guardian2'

if __name__== "__main__":

    # Create kafka consumer for topic
    consumer = KafkaConsumer(
    topic_name,
     bootstrap_servers=['localhost:9092'],
     value_deserializer=lambda x: loads(x.decode('utf-8')))
    for message in consumer:
            print(message)
