# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
# 最大公约数
def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print('Largest factor of %d is %d' %(num,count))
            break
        count -= 1
    else:
        print(num,'is prime')

for eachNum in range(10,21):
    showMaxFactor(eachNum)









# if __name__ == '__main__':