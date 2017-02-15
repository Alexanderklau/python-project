# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
def loop_merge_sort(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    tmp.extend(l1)
    tmp.extend(l2)
    print(set(tmp))
    return tmp
l1 = [2, 3, 8, 4, 9, 5, 6]
l2 = [5, 6, 10, 17, 11, 2]
loop_merge_sort(l1,l2)














# if __name__ == '__main__':