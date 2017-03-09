# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
class Foo:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def kanchai(self):
        print("%s,%s岁,%s,上山去砍柴" %(self.name, self.age, self.gender))

xiaoming = Foo('lau',20,'man')
xiaoming.kanchai()










# if __name__ == '__main__':