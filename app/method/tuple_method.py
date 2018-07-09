#!/usr/bin/env python
#Python 3.7.0 元祖常用方法
__author__ = "lrtao2010"

#元祖和列表类似，只不过元祖一旦被创建一级元素不可更改（增删改）。

# a = ('123',['abc'],'b',345,['6','7','d'],)
# a[-1][2] = 'c'
# print(a)
# a[-1].append(123)
# print(a)
# ('123', ['abc'], 'b', 345, ['6', '7', 'c'])
# ('123', ['abc'], 'b', 345, ['6', '7', 'c', 123])

# a = ('123',['abc'],'b',345,['6','7','d'],)
# a[0] = '456'
# print(a)
#     a[0] = '456'
# TypeError: 'tuple' object does not support item assignment


#a = ('123','a',123，['a','b','c'],)
#元祖最后一个元素后面一般加上','号

# a = ('123',['abc'],'b',345,['6','7','d'],)
# v1 = a[1]
# v2 = a[2:]
# v3 = a[1:-1]
# print(v1)
# print(v2)
# print(v3)
# ['abc']
# ('b', 345, ['6', '7', 'd'])
# (['abc'], 'b', 345)

#可迭代
# a = ('123',['abc'],'b',345,['6','7','d'],)
# for i in a:
#     print(i)
#
# 123
# ['abc']
# b
# 345
# ['6', '7', 'd']

#count 统计指定值出现的次数
# a = ('a','b','a',['a','b','ab'],'ab',)
# v1 = a.count('a')
# v2 = a[3].count('b')
# print(v1,v2)
# 2 1


# index(self, *args, **kwargs)查找指定值的位置，不存在会报错
# a = ('a','b')
# v = a.index('b')
# print(v)
# 1
