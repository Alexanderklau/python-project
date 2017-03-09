# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests
from bs4 import BeautifulSoup
class Url_List:
    def __init__(self,tite):
        self.tite = tite
        # self.page = page
    def Url(self):
        # https://www.baidu.com/s?wd=%E4%BD%A0%E5%8F%B7
        url = 'https://www.baidu.com/s?wd=' + self.tite
        print(url)










# if __name__ == '__main__':