# -*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
# title = re.compile('<title>(.*?)</title>',re.S)
wb_data = requests.get('http://www.sina.com.cn/')
wb_data.encoding = 'utf-8'
text = wb_data.text
# print(wb_data.text)
title = re.findall('<title>(.*?)</title>',wb_data.text,re.S)[0]
print(title)

