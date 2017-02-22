# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

解题思路：
1：利润分级
I <= 100k,cash + (cash * 10%)
I >100k <= 200k (cash - 10 * 7.5%) + 10 * 10%
"""
import math
#单位 万元
cash = int(input('Enter number>: '))
if cash <= 10:
    rich = cash * 0.1
    print(rich,'万元')
elif cash > 10 and cash <= 20:
    rich = (cash-10) * 0.75 + 10 * 0.1
    print(rich,'万元')
elif cash > 10 and cash > 20 and cash <= 40:
    rich = (cash-20) * 0.5 + 10 * 0.1 + (cash - 20 - 10) * 0.75
    print(rich,'万元')













# if __name__ == '__main__':