# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
题目：要求输出国际象棋棋盘。
"""
for i in range(1,9):
    for j in range(1,9):
        if (i + j) % 2 == 0:
            print('white')
        else:
            print('Black')









# if __name__ == '__main__':