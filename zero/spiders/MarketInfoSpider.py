# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class MarketinfospiderSpider(scrapy.Spider):
    """
    
    """
    name = 'MarketInfoSpider'
    allowed_domains = ['www.csindex.com.cn','www.shibor.org']
    start_urls = ['http://www.csindex.com.cn/','http://www.shibor.org/shibor/web/html/shibor.html']

    def start_request(self):
        shiborRequest=Request(url="http://www.shibor.org/shibor/web/html/shibor.html",callback=self.parse_shibor)

    def parse_shibor(self):
        pass

    def parse(self, response):
        print(response.url)
