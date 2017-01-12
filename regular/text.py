import re
import requests
from bs4 import BeautifulSoup
import time
# url = 'http://www.tt51.cn/mm/index.html'
# wb_data = requests.get(url)
# wb_data.encoding = 'utf-8'
# print(wb_data.text)
# def ImageListUrl(nation,pagenum):
#     # http: // www.tt51.cn / model / index.html
#     url = 'http://www.tt51.cn/' + str(nation) + '/index' + str(pagenum) + '.html'
#     wb_data = requests.get(url)
#     wb_data.encoding = 'utf-8'
#     soup = BeautifulSoup(wb_data.text,'lxml')
#     links = soup.select('a.imageLink')
#     for link in links:
#         href = link.get('href')
#     return href
def download(url):
    wb_data = requests.get(url)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text,'lxml')
    href = soup.select('div.main-body a')
    link = href.get('href')
    print(link)

download('http://www.tt51.cn/model/1853.html')

# if __name__ == "__main__":
#     print("""
#     ===============================
#     japan  model  taiwan  mm  share
#     ===============================
#     """)
#     ex = input('Please input a type:')
#     page = input('Please input a page:')
#     url = ImageListUrl(ex,page)

