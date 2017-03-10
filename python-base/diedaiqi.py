# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
class Simple(object):
    def __init__(self,step):
        self.step = step
    def next(self):
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step
    def __iter__(self):
        return self

for el in Simple(4):
    print(el)









# if __name__ == '__main__':