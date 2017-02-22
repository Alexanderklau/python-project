# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
a = 'abcindeaknmgkainsbe294771'
l = sorted(a)
# print(l)
a_upper = []
a_lower = []
for x in l:
    if x.isupper():
        a_upper.append(x)
    elif x.islower():
        a_lower.append(x)
    else:
        pass

for y in a_upper:
    y_lower = y.lower()
    if y_lower in a_lower:
        a_lower.insert(a_lower.index(y_lower),y)
print(''.join(a_lower))










# if __name__ == '__main__':