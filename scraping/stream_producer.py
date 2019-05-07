from newsplease import NewsPlease
from kafka import KafkaProducer
from time import sleep
import json, sys
from json import dumps
import requests
import time
import scrapy
import csv
from pymongo import MongoClient


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
    with open('links.csv','r') as in_file, open('links_distinct.csv','w') as out_file:
        seen = set()
        for line in in_file:
            if line in seen:
                continue # skip duplicate
            seen.add(line)
            out_file.write(line)
    with open('sample.csv', mode='w') as write_file:
        csv_writer=csv.writer(write_file)
        with open('test.csv', mode='rU') as read_file:
            for line in read_file:
                obj={}
                url=line.strip()
                article=NewsPlease.from_url(url)
                obj['title']=article.title
                obj["language"]=article.language
                obj["source_domain"]=article.source_domain
                obj["filename"]=article.filename
                obj["description"]=article.description
                obj["authors"]=article.authors
                obj["url"]=article.url
                obj["text"]=article.text
                json_obj=json.dumps(obj)
                csv_writer.writerow([json_obj])
                print(json_obj)
