# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
line =  'asdb sdier addf; dwd'
import re
x = re.split(r'[\s;,]\s*',line)
print(x)
fields = re.split(r'(;|,|\s)\s*',line)#捕获分组
print(fields)

values = fields[::2]
print(values)









# if __name__ == '__main__':