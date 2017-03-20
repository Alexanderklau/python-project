# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import os
# Input a file name
filename = input('>Enter file name: ')
# open file
fobj = open(filename,'w+')
# loop this project
while True:
    aLine = input("Enter a line('.' to quit): ")
    if aLine != ".":
        fobj.write('%s%s' % (aLine,os.linesep))
    else:
        break
fobj.close()










# if __name__ == '__main__':