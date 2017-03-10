# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'

dict = {'a':'lau','b':'alex','c':'yemilice'}
dicts = {'d':'aaa'}
print(dict.items())
for (k,v) in dict.items():
    print('dict[%s] =%s' % (k,v))

print(dict.get('a'))
dict.update(dicts)
print(dict)





# if __name__ == '__main__':