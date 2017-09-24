# -*- coding: utf-8 -*-
__author__ = 'yemilice_lau'
import builtwith
import urllib3
import urllib2
import re
import logging
# 获取到网页并且下载下来(urllib2)
"""
该爬虫可持续，并且可以捕获异常，并且可以灵活调用
"""
def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading:',url
    headers = {'User-agent':user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Downloading error!',e.reason
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries-1)
    return html


def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download(link)
    # return html

# download('http://httpstat.us/500')
crawl_sitemap('http://example.webscraping.com/sitemap.xml')