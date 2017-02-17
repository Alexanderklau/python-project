# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
def bubblesort(s):
    x=0
    N=0
    n=0
    while N<(len(s)-1):
        while n<(len(s)-1):
            if s[x]>s[x+1]:
                s[x],s[x+1] = s[x+1],s[x]
            x+=1
            n+=1
        x=0
        n=0
        N+=1
    return s








# if __name__ == '__main__':