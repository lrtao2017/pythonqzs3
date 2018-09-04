#!/usr/bin/env python
__author__ = "lrtao2010"

#python3.7 迭代器和生成器

#迭代器协议：
'''
1、迭代器协议是指：对象必须提供一个next方法，执行该方法要么返回迭代中的下一项，
要么就引起一个StopIteration异常，已终止迭代，只能往后走，不能往前退.
2、可迭代对象：实现了迭代器协议的对象（对象内部定义一个__iter__()方法）,节省内存
3、协议是一种约定，可迭代对象实现了迭代器协议，Python的内部工具（如for、sum、min、max等）
使用迭代器协议访问对象。
'''

#for 循环的强大功能
'''
字符串，列表，元祖，字典，集合。这些都不是可迭代对象（没有next方法），在for 循环中，调用了他们的内部
__iter__方法，把他们变成了可迭代对象。
for循环调用可迭代对象的__next__方法去取值，并且for 循环可以捕捉StopIteration异常，终止迭代。

'''
# l_test=[1,2,3]
# iter_l_test=l_test.__iter__()
# print(iter_l_test.__next__())
# print(iter_l_test.__next__())
# print(iter_l_test.__next__())
# print(iter_l_test.__next__())
# # 1
# # 2
# # 3
# # Traceback (most recent call last):
# #   File "D:/python3/app/Module_and_Functions/iterator_and_generator.py", line 28, in <module>
# #     print(iter_l_test.__next__())
# # StopIteration

#用whilex循环模拟for循环
# l_test=[1,2,3]
# iter_l_test=l_test.__iter__()
# while True:
#     try:
#         #print(iter_l_test.__next__())
#         print(next(iter_l_test))
#     except StopIteration:
#         #print('end')
#         break

#生成器
'''
生成器也是一种数据类型，这种数据类型自动实现了“迭代器协议”，生成器是可迭代对象。

生成器分类：
1、生成器函数：常规函数定义，但是使用yield语句而不是return 语句返回结果，yield语句
一次返回一个结果，可以使用多次，在每个结果中间，挂起函数的状态，以便下次从它离开的地方
继续执行。

2、生成器表达式：类似列表推导式，生成器返回按需产生结果的一个对象，而不是一次构建
一个完整的结果列表

生成器优点:
在需要的时候才产生结果，不是立即产生结果
'''

#生成器函数
# def g_test():
#     yield 1
#     yield 2
#     yield 3
# g_test1=g_test()
# print(g_test1)
# print(g_test1.__next__())
# print(g_test1.__next__())
# print(g_test1.__next__())
# # <generator object g_test at 0x0000000002163570>
# # 1
# # 2
# # 3

#生成器表达式，大数据不会占用大内存
# l_g = ('%s' %i for i in range(10) if i%2 == 0)
# print(l_g)
# print(l_g.__next__())
# print(l_g.__next__())
#print(next(l_g))
# print(l_g.__next__())
# <generator object <genexpr> at 0x0000000002133570>
# 0
# 2
# 4
# 6


#三元表达式
# name = 'example'
# res='True' if name == 'example' else 'False'
# print(res)
# True

#列表解析,大数据占用内存比较大
# l_test1=['%s' %i for i in range(10)]
# l_test2=['%s' %i for i in range(10) if i%2 == 0]
# print(l_test1)
# print(l_test2)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# ['0', '2', '4', '6', '8']

#生成器总结
'''
1、节省内存
2、提高代码可读性
3、只能遍历一次，只能遍历一次，只能遍历一次
'''