# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from sys import argv

script,filename = argv

print("We're going to earse %r." %filename)
print("If u want exit,please input ctrl-c")
print("If you do want that,hit RETURN")

input("?")

print("Open this file.....")

target = open(filename,'a+')

print("Truncating the file.Goodbye!")

target.truncate()

print("Now i'm going to ask u for three lines")

line1 = input("line1:")

print("i'm going to write these to the file.")

target.write(line1)
target.write('\n')

print("And this, we close it.")



target.close()











# if __name__ == '__main__':