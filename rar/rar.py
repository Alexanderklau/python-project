# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import os

for i in range(0, 1000000):
    p = str(i)
    cmd = "winrar e xxx.rar -y -p%s" % (p)

    r = os.system(cmd)
    if r == 1 or r == 0:
        print("pass = %s" % p)
        break

    print("%s %d" % (p, r))








# if __name__ == '__main__':