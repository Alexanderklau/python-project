# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
cites = {
    'lau':'wenbo',
    'st':'alex'
}
cites['lau'] = 'ttt'
print('-'*100)
print(cites)
state = cites.get('TExt',None)
print(state)
for cite in cites.items():
    print(cite)








# if __name__ == '__main__':