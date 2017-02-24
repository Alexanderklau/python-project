# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'

def quickfort(lst):
    if lst:
        l = lst.pop()
        x = []
        y = []
        while lst:
            m = lst.pop()
            if m > l:
                x.append(m)
            else:
                y.append(m)
        if x:
            quickfort(x)
            lst.append(x)
        lst.append(l)
        if y:
            quickfort(y)
            lst.extend(y)
    return lst








if __name__ == '__main__':
    t = input()
    quickfort(t)
