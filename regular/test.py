import requests
from bs4 import BeautifulSoup


def getpage(url):
    url = 'http://www.tt51.cn/model/index2.html'
    wb_data = requests.get(url)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for link in soup.select('a.imageLink'):
        ImageUrl = link.get('href')
        return ImageUrl
getpage('http://www.tt51.cn/model/index2.html')