# -*- coding: utf-8 -*-
import scrapy


class MarketinfospiderSpider(scrapy.Spider):
    name = 'MarketInfoSpider'
    allowed_domains = ['www.csindex.com.cn']
    start_urls = ['http://www.csindex.com.cn/']

    def parse(self, response):
        pass
