# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
from zero.utils import datetime_to_str


class ZeroItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    def convert(self):
        """
        完成对数据项的清理，数据类型转换，并返回字典
        """
        data=dict(self)
        return data

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
    unit                    =scrapy.Field()

    def convert(self):
        dc=dict(self)
        #定义要做数据类型转换的k值，把str 转换成float
        res={}
        ks=['new_investor','final_investor','new_natural_person','new_non_natural_person',
            'final_natural_person','final_non_natural_person']
            
        if '万' in dc['unit']:
            for k in ks:
                res[k]=float(dc[k].replace(',','')) *10000
            res['push_date']=dc['push_date']
        return res

    pass


class IndexCollectorItem(ZeroItem):
    push_date               =scrapy.Field()
    index_name              =scrapy.Field()
    open_value              =scrapy.Field()
    close_value             =scrapy.Field()
    higest_value            =scrapy.Field()
    lowest_value            =scrapy.Field()
    fluctuation             =scrapy.Field()
    total_market_value      =scrapy.Field()
    transaction_amount      =scrapy.Field()
    circulation_market_value=scrapy.Field()

    def convert(self):
        data=dict(self)
        res={}
        for k in data:
            if k not in ['push_date','index_name']:
                res[k]=float(data[k]) if len(data[k]) != 0 else 0
        res['push_date']=datetime_to_str(data['push_date'])
        res['index_name']=data['index_name']
        return res

class IndexStatisticItem(ZeroItem):
    push_date=scrapy.Field()
    index_name=scrapy.Field()
    spe=scrapy.Field()
    dpe=scrapy.Field()
    pb =scrapy.Field()
    dp =scrapy.Field()
    lyspe=scrapy.Field()
    lydpe=scrapy.Field()
    lypb=scrapy.Field()

    def convert(self):
        data=dict(self)
        return data


class FoundationBriefItem(ZeroItem):
    found_code           =scrapy.Field()
    found_name           =scrapy.Field()
    found_manager_user   =scrapy.Field()
    found_manager_company=scrapy.Field()
    found_type           =scrapy.Field()
    found_birth          =scrapy.Field()
    found_exchange       =scrapy.Field()

    def convert(self):
        data=dict(self)
        if data['found_birth']=='':
            data['found_birth']='1000-01-01'
        return data