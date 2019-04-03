import re
from pymongo import MongoClient
ip = input('使用默认IP(回车键)或重新输入>>')
host='192.168.3.31'
if ip:
    host=ip

client = MongoClient(host=host,port=27017)
collection = client['GuShiWen']['poem']
while True:
    name = input('输入诗名:')
    if name=='':
        break
    t = collection.find_one({'name':name})
    t = dict(t)
    for key,val in t.items():
        if key == '_id'or key=='name':
            continue
        if key=='dynasty':
            key='朝代:'
            print(key, val)
        elif key=='author':
            key = '作者:'
            print(key, val)
        elif key == 'url':
            key = '网址:'
            print(key, val)
        elif key =='content':
            key = '内容:'
            print(key,val)
        else:
            print(key)
            print(val.strip())
        # print(value)
