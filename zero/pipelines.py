# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import zero.poster as     poster
from   zero        import items

post_router={
    items.ShiborItem:poster.ShiborItemPoster,
    items.InvestorSituationItem:poster.InvestorSituationItemPoster,
    items.indexCollectorItem:poster.indexCollectorItemPoster,
}


class ZeroPipeline(object):
    def process_item(self, item, spider):
        post_router[item.__class__](item).post()
        return item
