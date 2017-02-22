# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
输入三个整数x,y,z，请把这三个数由小到大输出。
分析
1：先输入三个数
2：利用内置函数max比较
3：循环一次
"""
w = []
x = int(input("请你输入要比较数字总共的数量："))
for i in range(x):
    a = int(input("请输入你要比较的数字:"))
    w.append(a)
print("输入结束等待结果")
while 1:
    try:
        c = max(w)
        w.remove(c)
        print(c)
    except ValueError:
        print(" 程序已经结束")
        break







        # if __name__ == '__main__':