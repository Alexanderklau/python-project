import requests
from bs4 import BeautifulSoup
import time
from urllib.request import urlopen
import re
import random
class Spider(object):
    def __init__(self):
        print("""
        =======================
              开始下载图片
        =======================
        """)
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        proxy_list = ['http://222.169.193.162:8099',
                           'http://171.38.154.86:8123',
                           'http://60.176.164.2:8118',
                           'http://180.104.106.130:8998',]
        proxy_ip = random.choice(proxy_list)
        self.proxies = {'http:':proxy_ip}

    def getHtml(self,url):
        wb_data = requests.get(url,headers = self.headers,proxies = self.proxies)
        wb_data.encoding = 'utf-8'
        html = wb_data.text
        return html
    def getPagenum(self,url,total_page):
        now_page = int(re.search('index(\d+)',url,re.S).group(1))
        page_group = []
        for i in range(now_page,total_page + 1):
            link = re.sub('index\d+','index%s' %i,url,re.S)
            page_group.append(link)
            # print(page_group)
        return page_group
    def getImageUrl(self,url):
        wb_data = requests.get(url)
        wb_data.encoding = 'utf-8'
        soup = BeautifulSoup(wb_data.text,'lxml')
        for link in soup.select('a.imageLink'):
            ImageUrl = link.get('href')
            data = requests.get(ImageUrl)
            html = BeautifulSoup(data.text,'lxml')
            lites = html.select('div.main-body a img')
            title = html.select('h2')[0]
            for lite in lites:
                href = lite.get('src')
                cs = urlopen(href)
                f = open(r'Girl/' + title + '.jpg', "wb")
                f.write(cs.read())
                f.close()
    # def DownloadImage(self,url):
    #     wb_data = requests.get(url)
    #     wb_data.encoding = 'utf-8'
    #     soup = BeautifulSoup(wb_data.text,'lxml')
    #     links = soup.select('div.main-body a img')
    #     title = soup.select('h2')[0]
    #     for link in links:
    #         href = link.get('src')
    #         connect = urlopen(href)
    #         f = open(r'Girl/'+ title + '.jpg', "wb")
    #         f.write(connect.read())
    #         f.close()
if __name__ == '__main__':
    classinfo = []
    url = 'http://www.tt51.cn/model/index1.html'
    imageSpider = Spider()
    all_links = imageSpider.getPagenum(url,20)
    for link in all_links:
        imageSpider.getImageUrl(link)
    # for link in all_links:
    #     htmls = imageSpider.getImageUrl(link)
    #     print(htmls)
    #     # for html in htmls:
    #     #     imageSpider.DownloadImage(html)


