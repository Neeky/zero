# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZeroItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    def convert(self):
        """
        完成对数据项的清理，数据类型转换，并返回字典
        """
        raise NotImplemented()

class ShiborItem(ZeroItem):
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
        dc=dict(self)
        ks=['one_night','one_week','two_week','one_month','three_month',
            'six_month','nine_month','one_year']
        for k in ks:
            dc[k]=float(dc[k])
        dc['push_date']=dc['push_date'][:10]
        return dc

class InvestorSituationItem(ZeroItem):
    push_date               =scrapy.Field()
    new_investor            =scrapy.Field()
    final_investor          =scrapy.Field()
    new_natural_person      =scrapy.Field()
    new_non_natural_person  =scrapy.Field()
    final_natural_person    =scrapy.Field()
    final_non_natural_person=scrapy.Field()

    def convert(self):
        dc=dict(self)
        #定义要做数据类型转换的k值，把str 转换成float
        ks=['new_investor','final_investor','new_natural_person','new_non_natural_person',
            'final_natural_person','final_non_natural_person']
        for k in ks:
            dc[k]=float(dc[k].replace(',',''))      
        return dc
