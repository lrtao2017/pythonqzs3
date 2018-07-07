#!/usr/bin/env python
##Python 3 列表常用方法
__author__ = "lrtao2010" 

#创建列表
# a = []
# b = [1,2,3]
# c = list('123')
# print(a)
# print(b)
# print(c)
# []
# [1, 2, 3]
# ['1', '2', '3']

#list()将其他类型转换成列表
# a = list('123')
# b = list('thisistest')
# c = list('this is test')
# print(a)
# print(b)
# print(c)
# ['1', '2', '3']
# ['t', 'h', 'i', 's', 'i', 's', 't', 'e', 's', 't']
# ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 't', 'e', 's', 't']

# a = list(123)
# print(a)
#     a = list(123)
# TypeError: 'int' object is not iterable


#使用[offset]获取元素 或 修改元素,数组越界会报错
#a = ['a1','b1','c1']

# print(a[1])
# b1

# a[1] = 'd1'
# print(a)
# ['a1', 'd1', 'c1']

# print(a[3])
#     print(a[3])
# IndexError: list index out of range

a = list('abcdefg')
# print(a)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
