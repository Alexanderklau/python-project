# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
继承，面向对象中的继承和现实生活中的继承相同，即：子可以继承父的内容
"""
class JC:
    def eat(self):
        print("%s eat" %self.name)
    def drink(self):
        print("%s drink" %self.name)
    def shit(self):
        print("%s shit" %self.name)

class cat(JC):
    def __init__(self,name):
        self.name = name
        self.breed = 'cat'
    def crt(self):
        print('AKAKAK')
        print('cat name %s ' %(self.name))

c1 = cat('white cat')
c1.eat()
c1.crt()








# if __name__ == '__main__':