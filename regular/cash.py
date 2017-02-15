# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import re
def re_demo():
    txt = 'IF nmow dad fvda d adada 100 sets,the da $9.90'
    m = re.search(r'(\d).*\$(\d+\.?\d*)',txt)
    print(m.group())




if __name__ == '__main__':
    re_demo()