
import requests
import argparse
import csv
from os import path
import os



class FileLoader(object):
    server_url="http://www.financedatas.com/component/"
    api="market/add/update/stockindex/"

    kvmaping={
        'index_name':1,
        'push_date' :2,
        'open_value':5,
        'higest_value':7,
        'lowest_value':8,
        'close_value':9,
        'fluctuation':11,
        'transaction_amount':12}


    @property
    def http_api(self):
        return self.server_url+self.api

    @staticmethod
    def strQ2B(ustring):
        """把全角转化为半角
        """
        rstring=""
        for uchar in ustring:
            inside_code=ord(uchar)
            if inside_code == 12288:
                inside_code=32
            elif (inside_code >= 65281 and inside_code <= 65374):
                inside_code= inside_code-65248
            rstring+=chr(inside_code)
        return rstring

    def genData(self,cvs_line):
        data={}
        for k in self.kvmaping:
            if k in ['index_name','push_date']:
                data[k]=self.strQ2B(cvs_line[self.kvmaping[k]]).strip()
            else:
                data[k]=float(self.strQ2B(cvs_line[self.kvmaping[k]]))
        return data

    def __init__(self,csv_line):
        self.datas=[self.genData(data) for data in csv_line]

    @classmethod
    def ReadFiles(cls,source=None,encoding='gbk'):
        if source == None:
            raise ValueError("source can not be None")
        if path.isdir(source):
            files=os.listdir(source)
            abs_file_paths=[path.join(source,file_name) for file_name in files]
            for file_path in abs_file_paths:
                print(file_path)
                reader=csv.reader(open(file_path,'r',encoding=encoding))
                lines=[line for line in reader][1:]
                yield cls(lines)
        elif path.isfile(source):
            reader=csv.reader(open(source,'r',encoding=encoding))
            lines=[line for line in reader][1:]
            yield cls(lines)

    def post(self):
        for data in self.datas:
            response=requests.post(self.http_api,data=data)
            print(data)
            print(response.text)
        


    


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',help='文件所在目录|或文件全路径',default="/Users/jianglexing/Downloads/sh_hq_000016_2004_2017/")
    parser.add_argument('--encoding',help='编码',default="gbk")
    args=parser.parse_args()
    for loader in FileLoader.ReadFiles(args.source,encoding=args.encoding):
        loader.post()
    
        

        