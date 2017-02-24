# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
myjob = "hacker"
for c in myjob:print(c,end=' ')
a = [1,2,3,4,5]
s = 'Hello'
s = s.replace('ll','xx')
print(s)

s1 = s[:2] + 'txtdsasd' + s[10:]
print(s1)
s2 = ''.join([s1])

print(s2)
s3 = 'SPAM'.join(['eggs','squfeg','dsadw'])
print(s3)

s4 = 'Bob,hacker,nned'
s4 = s4.split(',')
s4 = ''.join(s4)
print(s4)

s5 = "the is de is \n"
s5.rstrip()
print(s5)

s6 = s5.upper()
print(s6)

print('{}/{}'.format(42,21))







# if __name__ == '__main__':