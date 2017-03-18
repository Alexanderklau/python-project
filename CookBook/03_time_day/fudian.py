# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
你想对浮点数执行指定精度的舍入运算。
"""
# _a = 2.3
# _b = 3.1
# print(_a + _b)
# from decimal import Decimal
# a = Decimal('2.3')
# b = Decimal('3.1')
# print(a + b)
# def squares(x):
#     for i in range(x):
#         yield i ** 2
#
# squares(10)
def func():
    x  = 4
    action = (lambda n:x ** n)
    print(action)
    return action
x = func()
print(x(2))










# if __name__ == '__main__':