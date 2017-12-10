# -*- encoding: utf-8 -*-
import scrapy
import codecs
from myscrap.items import MyscrapItem

 
class BookSpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['spys.one']
    start_urls = ['http://spys.one/proxies/']
	

    def parse(self, response):
        rows = response.xpath('.//td[@align="center"]/table/tr')
        i=3
        while i < len(rows)-1:
            item = MyscrapItem()
            row=rows[i]
            item['id'] = row.xpath ('td/font/text()').extract()[0]
            item['proxy_address'] = row.xpath ('td/font/text()').extract()[1]
            i=i+1
            yield item   


		