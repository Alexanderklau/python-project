# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import re
a = r'12312《中国》dhdsanihjaosdaudanxcxjajksjd'
patten = re.compile(r'《.*?》')
matcher = re.search(patten,a)
print(matcher.group(0))



