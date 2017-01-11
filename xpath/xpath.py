from lxml import etree
import requests
from bs4 import BeautifulSoup


html = requests.get('http://www.sina.com.cn/')
Selector = etree.HTML(html)

title = Selector.xpath('//title')
print(title)