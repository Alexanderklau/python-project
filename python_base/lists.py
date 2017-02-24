# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
L = ['abc','ABD','Abe']
L.sort()#排序，按字母顺序
print(L)

L.sort(key=str.lower)
print(L)

X = [1,2]
X.extend([3,4,5])
print(X)

X.pop()#去掉最后一位

X.reverse()
print(X)







# if __name__ == '__main__':