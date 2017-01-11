import re
import requests
from bs4 import BeautifulSoup

wb_data = requests.get('http://www.sina.com.cn/')
html = BeautifulSoup(wb_data.text, 'lxml')
title = re.search('<title>(.*?)</title>', html, re.S)
print(title)