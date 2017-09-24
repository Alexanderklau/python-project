# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests
from lxml import etree
html = requests.get('http://cuiqingcai.com/category/technique/python')
Selector = etree.HTML(html.text)
content = Selector.xpath('//img[@class="thumb"]/@alt')
ls = Selector.xpath('//span[starts-with(@class,"note")]/text()')[0]
info = ls.xpath('string(.)')
content_2 = info.replace('\n','').replace(' ','')
print(content_2)
for each in content:
    print(each)
for each in ls:
    print(each)









# if __name__ == '__main__':
