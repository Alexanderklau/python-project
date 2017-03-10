# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
# def facnia():
#     a,b = 0,1
#     while True:
#         yield b
#         a,b = b,a+b
#
# fib = facnia()
# print([fib.__next__() for i in range(10)])
iter = (x for x in range(10))
for el in iter:
    print(el)

for i in range(10):
    print(i)








# if __name__ == '__main__':