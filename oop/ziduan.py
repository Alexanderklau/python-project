# -*-coding:utf-8 -*-

__author__ = 'Yemilice_lau'
class Province:
    country = '中国'

    def __init__(self, name):

        # 普通字段
        self.name = name


# 直接访问普通字段
obj = Province('河北省')
print(obj.name)
Province.country









# if __name__ == '__main__':