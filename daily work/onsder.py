# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import os
def myfork():
    pid = os.fork()
    if pid == 0:
        print("This is child %d" %pid)
    else:
        print("This is parent %d" %pid)
if __name__ == '__main__':
    myfork()









# if __name == '__main__':