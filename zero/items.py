# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZeroItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ShiborItem(scrapy.Item):
    push_date  =scrapy.Field()
    one_night  =scrapy.Field()
    one_week   =scrapy.Field()
    two_week   =scrapy.Field()
    one_month  =scrapy.Field()
    three_month=scrapy.Field()
    six_month  =scrapy.Field()
    nine_month =scrapy.Field()
    one_year   =scrapy.Field()

    def convert(self):
        return dict(self)