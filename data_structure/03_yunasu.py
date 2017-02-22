# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
"""
查找最大或最小的 N 个元素
"""
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(len(nums),nums))
print(heapq.nsmallest(len(nums),nums))
print(heapq.heapify(nums))







# if __name__ == '__main__':