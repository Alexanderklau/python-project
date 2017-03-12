# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from bs4 import BeautifulSoup
import re
import requests

html = requests.get('https://www.baidu.com/baidu?wd=%22http%3A%2F%2Fnews.baidu.com%22&tn=monline_4_dg&ie=utf-8')
bsobj = BeautifulSoup(html.text,'lxml')
print(bsobj)
find_text = bsobj.select('a mnav')
print(find_text)
# print(find_text)









# if __name__ == '__main__':