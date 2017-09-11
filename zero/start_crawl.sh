#!/bin/bash

target=$(dirname $0)
cd $target
scrapy crawl shiborSpider
scrapy crawl investorSituationSpider
scrapy crawl indexCollector
