# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from sys import argv
from os.path import exists

script,from_file,to_file = argv

print("Copying from %s to %s "%(from_file,to_file))

in_file = open(from_file)

indata = in_file.read()

print("The input file is %d bytes long" %len(indata))

#exists，如果存在to_file文件，就返回True，否则返回False
print("Does the output file exist? %r" %exists(to_file))

print("Ready,hit REUTRN to continue,CTRL-C to abort.")

input()

out_file = open(to_file,'w')
out_file.write(indata)

print('Aright!')

out_file.close()

in_file.close()










# if __name__ == '__main__':