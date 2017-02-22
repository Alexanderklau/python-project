# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
如果一个可迭代对象的元素个数超过变量个数时,会抛出一个 ValueError 。那么
怎样才能从这个可迭代对象中解压出 N 个元素出来?
"""
# 利用*号
# record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# name, email, *phone_numbers = record
# print(phone_numbers)
record = ('ACME', 50, 123.45, (12, 18, 2012))
name,*_,(*_,year) = record
print(year)




# if __name__ == '__main__':