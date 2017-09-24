# -*- coding: utf-8 -*-
__author__ = 'yemilice_lau'
import urllib2
import re
import urlparse
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

def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    print '------------------'
    return webpage_regex.findall(html)

def linl_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        print html
        for link in get_links(html):
            print link
            if re.match(link_regex, link):
                #去除重复链接
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

linl_crawler('http://example.webscraping.com/places/default','/(index|view)')