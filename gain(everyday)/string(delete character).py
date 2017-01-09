a = str(1230403012)
#找到第一个字符
b = a[0]
#删除第一个字符
a = a.strip(b)
print(a)
#判断第一个数是否是0
if b == 0:
    print('Yes')
else:
    print('No')
#判断字符串长度
if len(a) > 5:
    print('Long')
else:
    print('short')
#判断字符串前几位是否对应要求
t = input('Enter str')
x = str(t)
c = x[0]
d = x[1]
if len(x) >= 5:
    if c and d == '0':
        print('Never!')
    elif c == '0':
        print('not good!')
    elif c != 0:
        print('Good!')
    else:
        print('i dont know')
else:
    print('good')
#替换字符串内的数


