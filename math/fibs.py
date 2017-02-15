# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'

def fibs(num):
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result









# if __name == '__main__':