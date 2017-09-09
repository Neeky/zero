
import requests
import argparse
import csv

#server_url="http://www.financedatas.com/component/"
server_url="http://127.0.0.1:8000/component/"
api="market/add/update/stockindex/"

def http_api():
    return server_url+api

#定义csv各个键值的映射
kvmaping={
    'index_name':1,
    'push_date' :2,
    'open_value':5,
    'higest_value':7,
    'lowest_value':8,
    'close_value':9,
    'fluctuation':11,
    'transaction_amount':12
}

def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:          
            inside_code = 32 
        elif (inside_code >= 65281 and inside_code <= 65374):
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring

#由csv中的一行，创建出一个data项
def gen_data(line):
    data={}
    for k in kvmaping:
        if k in ['index_name','push_date']:
            data[k]=strQ2B(line[kvmaping[k]].strip())
        else:
            data[k]=float(strQ2B(line[kvmaping[k]]))
    return data


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--file-name',help='文件名',default="/Users/jianglexing/Downloads/sh_hq_000016_2004_2017/sh_hq_000016_2004.csv")
    parser.add_argument('--encoding',help='编码',default="gbk")
    args=parser.parse_args()
    reader = csv.reader(open(args.file_name,'r',encoding=args.encoding))
    lines=[line for line in reader][1:]
    for line in lines:
        data=gen_data(line)
        response=requests.post(http_api(),data=data)
        print('*'*64)
        print(response.text)
        print('*'*64)
    
        

        