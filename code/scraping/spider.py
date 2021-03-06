import scrapy
import csv
import re

class ExtractUrls(scrapy.Spider):

    name = "extract"
    def start_requests(self):

        with open('urls.csv', mode='rU') as guardian:
            for line in guardian:
                url=line.strip()
                yield scrapy.Request(url = url, callback = self.parse)

    # Parse function
    def parse(self, response):
        with open('links.csv', mode='a') as guardian:
            csv_writer=csv.writer(guardian)
            links = response.css('a::attr(href)').extract()
            for link in links:
                if(link.startswith('http') is False):
                    link=response.request.url+link
                m=re.search(r'\d+$',link)
                if (m is not None or link.endswith('.html')):
                    csv_writer.writerow([link])
