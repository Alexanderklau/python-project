# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
# x = [i for i in range(10)]
# for i in [i for i in range(10)]:
    # print(i)
# for i in range(1,10,2):
    # print(i)
seq = ["one",'two',"three"]
for i,element in enumerate(seq):
    seq[i] = '%d: %s' %(i,seq[i])
print(seq)
i = iter('abc')
print(i.__next__())
print(i.__next__())
c = 0
for i in range(10):
    c += 1
    print(c)











# if __name__ == '__main__':