# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
D = {'spam':2,'ham':1,'eggs':3}
#提取值排序
print(list(D.values()))
# items分割
print(x for x in list(D.items()))
# get
print(D.get('spam'))

D2 = {'muffn':5}
d2 = D.update(D2)
print(d2)

print(D['spam'])
for lang in D:
    print(lang,'\t',D[lang])










# if __name__ == '__main__':