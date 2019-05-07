from newsplease import NewsPlease
from kafka import KafkaProducer
from time import sleep
import json, sys
from json import dumps
import requests
import time
import scrapy
import csv


def getData():
    data = []
    labels = {}
    index = 0

    #getting number of pages in response
    url = 'https://www.elcolombiano.com/'
    jsonData = requests.get(url)
    print(jsonData)


def publish_message(producer_instance, value):
    try:
        producer_instance.send('guardian2',  value=value)
        producer_instance.flush()
        print('Message published successfully. Story number: ')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))

def parse(self, response):
    # Get anchor tags
    links = response.css('a::attr(href)').extract()
    for link in links:
        print(link)

def connect_kafka_producer():
    producer = None
    try:
        #producer = KafkaProducer(value_serializer=lambda v:json.dumps(v).encode('utf-8'),
        #bootstrap_servers=['localhost:9092'], api_version=(0, 10),linger_ms=10)
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                 value_serializer=lambda x:
                                 dumps(x).encode('utf-8'))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return producer

if __name__== "__main__":
    with open('links.csv', mode='rU') as guardian:
        for line in guardian:
            url=line.strip()
            article=NewsPlease.from_url(url)
            print(article.title)
