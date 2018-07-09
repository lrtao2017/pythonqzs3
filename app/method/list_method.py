#!/usr/bin/env python
#Python 3.7.0 列表常用方法
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

#列表切片与提取元素list[start:end:step]
# a = list('abcdefghijk')
# v1 = a[2:3]
# v2 = a[2:]
# v3 = a[:]
# v4 = a[0:6:2]
# print(v1)
# print(v2)
# print(v3)
# print(v4)
# ['c']
# ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
# ['a', 'c', 'e']

#append(self, *args, **kwargs) 添加元素至尾部
# a = ['a','b']
# a.append('c')
# print(a)
# ['a', 'b', 'c']

#insert(self, *args, **kwargs)在指定位置插入
# a = ['a',['a','b']]
# a.insert(0,'c')
# a[2].insert(0,'c')
# a.insert(-1,'append')
# print(a)
# ['c', 'a', 'append', ['c', 'a', 'b']]

#clear(self, *args, **kwargs)清空列表
# a = ['a','b']
# a.clear()
# print(a)
# []

#copy (影子)复制，只拷贝第一层，2层以上,都是拷贝元素的地址，浅复制
# a = ['a',['b']]
# b = a.copy()
# c = a
# d = a[:]
# a.append('d')
# a[1].append('c')
# print(a)
# print(b,b is a, b == a )
# print(c,c is a, c == a )
# print(d,d is a, d == a )
# ['a', ['b', 'c'], 'd']
# ['a', ['b', 'c']] False False
# ['a', ['b', 'c'], 'd'] True True
# ['a', ['b', 'c']] False False

# 深复制
# import copy
# a = ['a',['b']]
# b = copy.deepcopy(a)
# a.append('d')
# a[1].append('c')
# print(a)
# print(b)
# ['a', ['b', 'c'], 'd']
# ['a', ['b']]

#count 统计指定值出现的次数
# a = ['a','b','a',['a','b','ab'],'ab']
# v1 = a.count('a')
# v2 = a[3].count('b')
# print(v1,v2)
# 2 1

#extend(self, *args, **kwargs) 合并列表同+=
# a = ['a']
# b = ['b']
# a.extend(b)
# print(a,b)
# ['a', 'b'] ['b']

# a = ['a']
# b = ['b']
# a += b
# print(a,b)
# ['a', 'b'] ['b']

# index(self, *args, **kwargs)查找指定值的位置，不存在会报错
# a = ['a','b']
# v = a.index('b')
# print(v)
# 1

# a = ['a','b']
# v = a.index('c')
# print(v)
#     v = a.index('c')
# ValueError: 'c' is not in list


#使用in判断值是否存在列表
# a = ['a']
# v1 = 'a' in a
# v2 = 'b' in a
# print(v1,v2)
# True False

# pop(self, *args, **kwargs) 返回某个元素后，并在数组里删除它。默认删除最后一个元素
# a = ['1','2','3']
# v = a.pop()
# print(a,v)
# ['1', '2'] 3

# a = ['1','2','3']
# v = a.pop(1)
# print(a,v)
# ['1', '3'] 2

#remove(self, *args, **kwargs) 删除最先找到的元素，找不到会抛异常
# a = ['1','2','3','2']
# v = a.remove('2')
# print(a,v)
# ['1', '3', '2'] None

# a = ['1','2','3','2']
# v = a.remove('0')
# print(a,v)
#     v = a.remove('0')
# ValueError: list.remove(x): x not in list

#reverse(self, *args, **kwargs)将列表翻转

# a = ['1','4','2','3','5']
# a.reverse()
# print(a)
# ['5', '3', '2', '4', '1']

#sort(self, *args, **kwargs) 排序，默认升序，和reverse()配合使用, 也可以降序
# a = ['1','4','2','3','5']
# a.sort()
# print(a)
# ['1', '2', '3', '4', '5']

# a = ['1','4','2','3','5']
# a.sort()
# a.reverse()
# print(a)
# ['5', '4', '3', '2', '1']

# a = ['1','4','2','3','5']
# a.sort(reverse=True)
# print(a)
# ['5', '4', '3', '2', '1']

##########################################################
#支持for、while循环
# a = ['1','2','3']
# for i in a:
#     print(i)
#
#
#i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

#修改（替换元素）
# test = ['a','b','c']
# test[1] = 0
# print(test)
# ['a', 0, 'c']

#删除指定元素
# test = ['a','b','c']
# del test[2]
# print(test)
# ['a', 'b']

