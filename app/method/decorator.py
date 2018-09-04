#!/usr/bin/env python
__author__ = "lrtao2010"

#python3.7 装饰器

#装饰器
'''
定义：本质就是一个函数，作用是为其他函数添加新的功能。
遵循的原则:
1、不改变被修饰函数的源代码（开放封闭原则）；
2、为被装饰函数添加新功能后，不修改被修饰函数的调用方式。
'''
#装饰器=高阶函数 + 函数嵌套 + 闭包

#高阶函数
'''
定义：
1、函数接收的参数是一个函数名；
2、函数的返回值是一函数名；
3、满足上述条件任意一个，都称之为高阶函数
'''

#函数嵌套
#在一个函数中再定义一个函数，并调用该函数

#闭包
#在一个作用域里放入定义的变量，相当于打了一个包

# import time
#
# def run_time(func):
#     def wrapper():
#         star_time = time.time()
#         func()
#         stop_time = time.time()
#         print("运行时间是%s" %(stop_time - star_time))
#     return wrapper
#
# @run_time
# #@ 语法糖  @run_time 等同于执行test=run_time(example),run_time(example)返回的是wrapper的地址
# def example():
#     time.sleep(3)
#     print('example run over')
#
# example()  #example() 执行的是wrapper()
#
# example run over
# 运行时间是3.0000040531158447
#
# import time
#
# def run_times(func):
#     def wrapper(*args):
#         star_time = time.time()
#         func(*args)
#         stop_time = time.time()
#         print("运行时间是%s" %(stop_time - star_time))
#     return wrapper
#
# @run_times
# def add(*args):
#     res=0
#     for i in args:
#         time.sleep(1)
#         res+=i
#     print(res)
# add(1,2,3,4,5,6,7,8,9,10)
#
# 55
# 运行时间是10.000013828277588
