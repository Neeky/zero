#!/bin/bash

wrkdir=$(dirname $0)
cd $wrkdir
#上证指数
python3 index_loader.py --source=/Users/jianglexing/Downloads/sh_hq_000001_2004_2017
#沪深300
python3 index_loader.py --source=/Users/jianglexing/Downloads/sz_hq_399300_2006_2017
#中证500
python3 index_loader.py --source=/Users/jianglexing/Downloads/sh_hq_000905_2007_2017
#上证50
python3 index_loader.py --source=/Users/jianglexing/Downloads/sh_hq_000016_2004_2017
#创业板指
python3 index_loader.py --source=/Users/jianglexing/Downloads/sz_hq_399006_2010_2017
#红利指数
python3 index_loader.py --source=/Users/jianglexing/Downloads/sh_hq_000015_2005_2017
#深证成指
python3 index_loader.py --source=/Users/jianglexing/Downloads/sz_hq_399001_2004_2017
