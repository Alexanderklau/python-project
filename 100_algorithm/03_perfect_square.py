# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少?
分析：
完全平方数？：一个数能表示成某个整数的平方的形式
1：写出完全平方数的求法
2：完全平方数判断
"""
[print(x**2-100,end=',') for x in range(1000) for y in range(1000) if (y ** 2 - x ** 2 == 168)]
"""
for x in range(1000):
 for y in range(1000):
  if (y ** 2 - x ** 2 == 168):
   print(x ** 2 - 100,end = '')
"""









# if __name__ == '__main__':