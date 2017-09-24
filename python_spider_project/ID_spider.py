# -*- coding: utf-8 -*-
__author__ = 'yemilice_lau'
import builtwith
import urllib3
import urllib2
import re
import logging
import itertools
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
#http://example.webscraping.com/places/default/view/81
"""
通过ID去爬取网页，遍历ID得到页面
"""
max_errors = 5
num_errors = 0
for page in itertools.count(1):
    url = 'http://example.webscraping.com/places/default/view/%d' % page
    html = download(url)
    if html is None:
        num_errors += 1
        if num_errors == max_errors:
            break
    else:
        num_errors = 0

