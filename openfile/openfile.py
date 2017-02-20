# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from sys import argv
#利用argv获取文件名
script,filename = argv

txt = open(filename)

print("Here's u file %r:" % filename)
#打开文件
print(txt.read())

print("Type the filename again")

file_again = input(">:")
#打开指定文件
txt_again = open(file_again)

print(txt_again.read())











# if __name__ == '__main__':