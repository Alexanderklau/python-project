# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import sys
def func():
    x = 4
    action = (lambda n: x ** n)
    # action = (lambda n: x ** n) 等同于
    # def action():
    #  return x ** n
    return action
x = func()
print(x(2))

foo = [1,2,3,4,5,6,7,8]
z = (filter(lambda x:x % 3 == 0,foo))

sys.stdout.write(str(z) + '\n')







# if __name__ == '__main__':