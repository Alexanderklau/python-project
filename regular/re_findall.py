import re
import requests
from bs4 import BeautifulSoup
import time

class GIspider:
    def __init__(self,baseUrl):
        self.baseUrl = baseUrl
        self.file = None
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
    def ImageListUrl(self,nation,pagenum):
        # http: // www.tt51.cn / model / index.html
        url = 'http://www.tt51.cn/' + str(nation) + '/index' + str(pagenum) + '.html'
        wb_data = requests.get(url,headers = self.headers)
        wb_data.encoding = 'urf-8'


