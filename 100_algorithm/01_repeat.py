# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
有1234个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
思路：
1.实现随机三位数
2.数字不重复
3.打印出数字
"""
sum = 0
for i in range(1,5):
    for x in range(1,5):
        for y in range(1,5):
            if(i != x & x != y):
                sum = sum + 1
                print(i,x,y)
print(sum)






# if __name__ == '__main__':