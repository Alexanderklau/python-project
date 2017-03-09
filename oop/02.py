# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
class Person:
    def __init__(self,na,gen,age,fig):
        self.name = na
        self.gender = gen
        self.age = age
        self.fight = fig
    def grassInd(self):
        self.fight = self.fight - 200
    def pratice(self):
        self.fight = self.fight + 200
    def incest(self):
        self.fight = self.fight - 500
    def datail(self):
        temp = "姓名:%s ; 性别:%s ; 年龄:%s ; 战斗力:%s" % (self.name, self.gender, self.age, self.fight)
        print(temp)
cang = Person('苍井井', '女', 18, 1000)
cang.datail()
cang.grassInd()
cang.datail()












# if __name__ == '__main__':