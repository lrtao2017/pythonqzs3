#!/usr/bin/env python
__author__ = "lrtao2010"

#Python 3.7.0 集合常用方法

#集合是无序的，元素不能重复，元素只能是数字、字符串、元祖
# a = set('abc')
# print(a)
# {'c', 'a', 'b'}

# a = {1,2,3,4,4,'abc',('a')}
# print(a)
# {1, 'abc', 2, 3, 4, 'a'}

# a = set(['hello','hello','tom','tom'])
# print(a)
# {'tom', 'hello'}

# add(self, *args, **kwargs)
# 向集合中添加一个元素，如果元素在集合中已经存在，可以执行，但不会再次添加
# a = {'a','b','c'}
# a.add(123)
# a.add('a')
# print(a)
# {'c', 123, 'b', 'a'}

#clear(self, *args, **kwargs)清空集合
# a = {'a','b','c'}
# a.clear()
# print(a)
# set()

#copy(self, *args, **kwargs) 浅复制
# a = {'a','b','c'}
# b = a.copy()
# print(b)
# a.add('d')
# print(a)
# print(b)

#pop(self, *args, **kwargs) 随机删除一个元素，并返回该元素，如果集合是空集合，报异常
# a = {'1','a',3}
# v = a.pop()
# print(v)
# print(a)
# a
# {3, '1'}

# a = {}
# a.pop()
# print(a)
#    a.pop()
# TypeError: pop expected at least 1 arguments, got 0

#remove(self, *args, **kwargs) 删除一个给定的元素，如果集合中没有该元素，报异常

# a = {'a',1,3}
# a.remove('a')
# print(a)
# {1, 3}

# a.remove('b')
#     a.remove('b')
# KeyError: 'b'

#discard(self, *args, **kwargs) 删除一个给定的元素，如果该元素不存在，什么也不做
# a = {'a',1,3}
# a.discard(1)
# a.discard(4)
# print(a)
# {'a', 3}

#定义不可变集合
# a = frozenset('Nochange')
# print(a)
# frozenset({'n', 'e', 'c', 'N', 'a', 'g', 'h', 'o'})

#列表去重，不考虑原来顺序
# name = ['tom','lilei','tom','jon','zdk']
# name = list(set(name))
# print(name)
# ['tom', 'jon', 'zdk', 'lilei']



##########集合关系运算########
# name_1 = {'tom','lilei','jim','jon'}
# name_2 = {'tom','bob','jhon','jon'}

#intersection(self, *args, **kwargs)求交集，并返回一个新集合，集合交换位置，结果一样
# name_3 = name_1.intersection(name_2)
# name_3 = name_1 & name_2
# print(name_1,name_2,name_3)
# {'jon', 'tom', 'jim', 'lilei'} {'bob', 'tom', 'jon', 'jhon'} {'jon', 'tom'}

#intersection_update(self, *args, **kwargs)
#将原集合修改为两个集合的交集
#name_1.intersection_update(name_2)
# name_1 = name_1 & name_2
# print(name_1,name_2)
# {'jon', 'tom'} {'jon', 'bob', 'jhon', 'tom'}



#union(self, *args, **kwargs) 求并集，并返回一个新集合,集合交换位置，结果一样
# name_3 = name_1.union(name_2)
# name_3 = name_1 | name_2
# print(name_1,name_2)
# print(name_3)
# {'tom', 'jon', 'jim', 'lilei'} {'tom', 'bob', 'jon', 'jhon'}
# {'jon', 'jim', 'tom', 'lilei', 'bob', 'jhon'}

#update(self, *args, **kwargs)
# 原集合更新为并集,
# name_1.update(name_2)
# print(name_1)
# print(name_2)
# {'lilei', 'jon', 'jim', 'bob', 'tom', 'jhon'}
# {'jhon', 'jon', 'bob', 'tom'}

# 也可以用作同时向集合中传入多个值（可以是元祖，列表，字符串（是可迭代对象即可））
#add 方法一次只能加入一个值
# a = {1}
# b = {'a'}
# c = {1,'b'}
# a.update((1,2,3,))
# b.update('abcd')
# c.update(['adb',123,('123',)])
# print(a)
# print(b)
# print(c)
# {1, 2, 3}
# {'c', 'a', 'd', 'b'}
# {1, 'adb', ('123',), 'b', 123}

#difference(self, *args, **kwargs)求差集，并返回一个新集合，集合交换位置，结果不一样
# name_3 = name_1.difference(name_2)
# name_4 = name_2.difference(name_1)
# name_3 = name_1 - name_2
# name_4 = name_2 - name_1
# print(name_1,name_2)
# print(name_3)
# print(name_4)
# {'jon', 'lilei', 'jim', 'tom'} {'jon', 'bob', 'jhon', 'tom'}
# {'jim', 'lilei'}
# {'bob', 'jhon'}

#difference_update(self, *args, **kwargs)
# 本集合中除去两个集合的交集，原集合被修改
# name_1.difference_update(name_2)
# name_1 = name_1 - name_2
# print(name_1,name_2)
# {'lilei', 'jim'} {'jon', 'jhon', 'bob', 'tom'}

#symmetric_difference(self, *args, **kwargs)
# 交叉补集=并集-交集，返回一个新集合，集合交换位置，结果一样
# name_3 = name_1.symmetric_difference(name_2)
# name_4 = name_2.symmetric_difference(name_1)
# name_3 = name_1 ^ name_2
# name_4 = name_2 ^ name_1
# print(name_1,name_2)
# print(name_3)
# print(name_4)
# {'jim', 'lilei', 'jon', 'tom'} {'jhon', 'jon', 'bob', 'tom'}
# {'jim', 'lilei', 'bob', 'jhon'}
# {'jim', 'lilei', 'bob', 'jhon'}

#symmetric_difference_update(self, *args, **kwargs)
#原集合修改为交叉补集
# name_1.symmetric_difference_update(name_2)
# print(name_1)
# print(name_2)
# {'jhon', 'lilei', 'jim', 'bob'}
# {'tom', 'jhon', 'bob', 'jon'}


#isdisjoint(self, *args, **kwargs)
# 如果两个集合没有交集(交集为空)返回True,集合交换位置，结果一样
# a = {1,2}
# b = {1}
# c = {3}

# a_b = a.isdisjoint(b)
# b_a = b.isdisjoint(a)
# a_c = a.isdisjoint(c)
# c_a = c.isdisjoint(a)
# print(a_b,b_a,a_c,c_a)
# False False True True

# a = {1,2,3}
# b = {1}
# c = {1,3,5}
#issubset(self, *args, **kwargs)是否为子集
# v1 = a.issubset(b)
# v2 = b.issubset(a)
# v3 = a.issubset(c)
# v4 = b <= a
# print(v1,v2,v3,v4)
# False True False True

#issuperset(self, *args, **kwargs)是否为父集
# v1 = a.issuperset(b)
# v2 = b.issuperset(a)
# v3 = a.issuperset(c)
# v4 = a >= b
# print(v1,v2,v3,v4)
# True False False True

