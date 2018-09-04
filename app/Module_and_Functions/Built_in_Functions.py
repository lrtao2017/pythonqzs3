#!/usr/bin/env python 
__author__ = "lrtao2010" 

#python3.7 内置函数整理

#abs(x)
#返回数字的绝对值。 参数可以是整数或浮点数。 如果参数是复数，则返回其大小
# print(abs(1))
# print(abs(-1))
# print(abs(-1.234))
# 1
# 1
# 1.234

#all(iterable)
#如果一个iterable(可迭代对象)的所有元素都为true（或者iterable为空），则返回True。
# a = all([1])
# b = all([])
# c = all([1,[],0])
# d = all(('a','b','c',))
# e = all(('',))
# f = all(('a','',))
# print(a,b,c,d,e,f)
# True True False True False False

#any(iterable)
#如果一个iterable的任一元素为true，则返回True。 如果iterable为空，则返回False。
# a = any([1])
# b = any([])
# g = any([0])
# c = any([1,[],0])
# d = any(('a','b','c',))
# e = any(('',))
# f = any(('a','',))
# print(a,b,g,c,d,e,f)
# True False False True True False True

#repr(object)
#class str(object='')
#class str(object=b'', encoding='utf-8', errors='strict')
#将任意值转换为字符串
#repr() 转化为供解释器读取的形式，得到的字符串通常可以用来重新获得该对象
#str() 用于将值转化为适于人阅读的形式，
# obj ='I love Python3.7'
# print(repr(obj))
# print(str(obj))
# print(obj == eval(repr(obj)))
# 'I love Python3.7'
# I love Python3.7
# True

#ascii(object)
#这个函数跟repr()函数一样，返回一个可打印的对象字符串方式表示。
# 当遇到非ASCII码时，就会输出\x，\u或\U等字符来表示。
# 与Python 2版本里的repr()是等效的函数。
# print(ascii('a'), ascii(10), ascii('u\中'))
# 'a' 10 'u\\\u4e2d'

#bin(x)
#十进制转二进制
# a = bin(16)
# b = bin(-16)
# print(a,b)
# 0b10000 -0b10000

#hex()
#十进制转十六进制
# a=hex(16)
# b=hex(-16)
# print(a,b)
# 0x10 -0x10

#oct()
#十进制转八进制
# a=oct(16)
# b=oct(-16)
# print(a,b)
# 0o20 -0o20



#class bool([x])
#返回一个布尔值，即True或False之一。
# 使用标准真值测试程序转换x。 如果x为false或省略，则返回False; 否则返回True
# a = bool(0)
# b = bool(1)
# c = bool(-1)
# d = bool("")
# print(a,b,c,d)
# False True True False

#breakpoint(*args, **kws)
#Python3.7带有一个名为breakpoint（）的内置函数，它在调用站点时进入调试器。
#虽然它是相同的结果，但它更直观和惯用。
# def divide(divisor, dividend):
#     breakpoint()     #出现异常后在（Pdb）后输入atgs(a),可以打印变量的具体值
#     return dividend / divisor
#
# if __name__ == '__main__':
#     print(divide(0, 4000))
# > e:\python\learning\app\module_and_functions\built_in_functions.py(84)divide()
# -> return dividend / divisor
# (Pdb) args
# divisor = 0
# dividend = 4000
# (Pdb)

#bytearray()
#返回一个可变byte数组

#bytes()
#返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。
# 它是 bytearray 的不可变版本

#chr()
#用一个范围在 0～1114111(0x10ffff)整数作参数，返回一个对应的Unicode字符。
# a=chr(98)
# print(a)
# b

#ord()
#返回一个字符串的Unicode 编码
# a=ord('b')
# print(a)
# 98

#callable()
#检查对象是否可以被调用

#############################类方法################################
#classmethod()
#是用来指定一个类的方法为类方法，没有此参数指定的类的方法为实例方法

# delattr()
# 用于删除属性

#getattr()
#用于返回一个对象属性，或者方法

#hasattr()
#确定一个对象是否具有某个属性。

#setattr()
#将值赋给属性的

#issubclass()
#issubclass(class,classinfo)
#判断参数 class 是否是类型参数 classinfo 的子类。

#property()
#作用是在新式类中返回属性值

#super() 函数是用于调用父类(超类)的一个方法

###################################################################
#compile()
#将一个字符串编译为字节代码

#complex() 返回一个复数
# a=complex(1,3)
# print(a)
# (1+3j)

#dict() 生成字典
# a=dict()
# b=dict(age=1,name='example')
# print(a)
# print(b)
# {}
# {'age': 1, 'name': 'example'}

#dir()
#不带参数时，返回当前范围内的变量、方法和定义的类型列表；
# 带参数时，返回参数的属性、方法列表。
# 如果参数包含方法__dir__()，该方法将被调用。
# 如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
# a=dir(tuple)
# print(a)
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']


#help()
#查看帮助信息
# a=help(tuple)
# print(a)
# class tuple(object)
#  |  tuple(iterable=(), /)
#  |
#  |  Built-in immutable sequence.
#  |
#  |  If no argument is given, the constructor returns an empty tuple.
#  |  If iterable is specified the tuple is initialized from iterable's items.

# divmod() 返回两个数的商和余数
# k,v = divmod(10,3)
# print(k,v)
# 3 1

#enumerate()
#用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中
#enumerate(sequence, [start=0])
# a=['name','age']
# for k,v in enumerate(a):
#     print(k,v)
# 0 name
# 1 age

#eval()
# 功能：将字符串str当成有效的表达式来求值并返回计算结果。
# 语法： eval(source[, globals[, locals]]) -> value
# 参数：
# source：一个Python表达式或函数compile()返回的代码对象
# globals：可选。必须是dictionary
# locals：可选。任意map对象
# a = '7*8'
# b=eval(a)
# print(b)
# 56
# a='{"name":"n"}'
# b=eval(a)
# print(a,type(a),b,type(b))
# {"name":"n"} <class 'str'> {'name': 'n'} <class 'dict'>

# exec()
# exec函数和eval函数类似，也是执行动态语句，
# 只不过eval函数只用于执行表达式求值，而exec函数主要用于执行语句块
# exec('a = 1 + 2')
# print(a)
# 3
# eval('a = 1 + 2')
# print(a)
# 3
# eval('a = 1 + 2')
# File
# "<string>", line
# 1
# a = 1 + 2
#   ^

#filter()
#接收一个函数和一个list，这个函数的作用是对每个元素进行判断，
# 返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，
# 返回由符合条件元素组成的新list。
# def is_odd(x):
#     return x % 2 == 1
# a = [1,2,3,4,5,6,7,8,9]
# b=list(filter(is_odd,a))
# print(a,b)
# [1, 2, 3, 4, 5, 6, 7, 8, 9] [1, 3, 5, 7, 9]

#map()将函数调用映射到每个序列的对应元素上并返回一个含有所有返回值的列表
# a = [1,2,3,4,5,6,7,8,9]
# b=list(map(lambda x:x*2,a))
# print(a,b)
# [1, 2, 3, 4, 5, 6, 7, 8, 9] [2, 4, 6, 8, 10, 12, 14, 16, 18]

#reduce()
#reduce函数会对参数序列中元素进行累积,
#在Python 3里,reduce()函数已经被从全局名字空间里移除了,
# 它现在被放置在fucntools模块里,用的话要先引入
# from functools import reduce
# a = [1,2,3,4,5,6,7,8,9]
# b=reduce(lambda x,y:x+y,a)
# print(a,b)
# [1, 2, 3, 4, 5, 6, 7, 8, 9] 45

#float()将数字或者可转换成数字的字符串转换成浮点数
# a=float(10)
# b=float('10')
# print(a,b)
# 10.0 10.0

#format()字符串格式化
# goods_c={'car':1200,'apple':200}
# for goods_n, goods_p in goods_c.items():
#     print('{:^7}'.format(goods_n), '{:<9}'.format(goods_p))
#   car   1200
#  apple  200
#set()集合（可变）
#frozenset() 不可变集合
# a=set(range(11))
# b=frozenset(range(11))
# print(a,type(a))
# print(b,type(b))
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10} <class 'set'>
# frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) <class 'frozenset'>

# globals()
# 返回一个全局变量的字典，包括所有导入的变量
# print(globals())

# locals()
#返回一个局部变量的字典

#vars()
#对象object的属性和属性值的字典对象，
#如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()


#hash() 返回一个不可变数据类型的hash 值
# test_hash = hash('example')
# print(test_hash)
# -4403578415847662099

#id()获取对象的内存地址
# a = 'example'
# print(id(a))
# 30823904

#input()接受一个标准输入数据，返回为 string 类型。
# a = input(">>>")
# print(a,type(a))
# >>>123
# 123 <class 'str'>

#int() int(x, base=10)
# 基数默认为10.有效基数为0和2-36。
# 基数0表示将字符串中的基数解释为整数文字。

# a=int(1)
# b=int('0x120',0)
# c=int('11',16)
# d=int('12',20)
# print(a,b,c,d)
# 1 288 17 22

#type()一个参数返回对象类型, 三个参数，返回新的类型对象。
# a = 123
# t_a=type(a)
# t_b=type(a) == int
# print(t_a,t_b)
# <class 'int'> True

#isinstance()
#isinstance() 判断一个对象是否是一个已知的类型，类似 type()
# a = 123
# is_a=isinstance(a,int)
# is_b=isinstance(a,str)
# is_c=isinstance(a,(int,str,tuple))
# print(is_a,is_b,is_c)
# True False True

#iter()
#用来生成迭代器

#next()
#next(iterator[, default])
# iterator -- 可迭代对象
# default -- 可选，用于设置在没有下一个元素时返回该默认值，
# 如果不设置，又没有下一个元素则会触发 StopIteration 异常。


#len() 返回长度
#list() 生成列表

#max() 返回最大值
#min() 返回最小值
# a=[10,34,5,67,]
# a_max=max(a)
# a_min=min(a)
# print(a_max,a_min)
# 67 5

#memoryview()
#返回给定参数的内存查看对象(Momory view)

#object()
#基类

#open()
#打开打开一个文件进行处理

#pow()
#Equivalent to x**y (with two arguments) or x**y % z (with three arguments)
# a = pow(2,3)
# b = pow(2,3,3)
# print(a,b)
# 8 2

#print()
#print(self, *args, sep=' ', end='\n', file=None)
# objects - - 复数，表示可以一次输出多个对象。输出多个对象时，需要用, 分隔。
# sep - - 用来间隔多个对象，默认值是一个空格。
# end - - 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
# file - - 要写入的文件对象。
# print('www','google','com',sep='.')
# www google com
# www.google.com

#range()创建一个整数列表
#range(start, stop[, step])
# for i in range(10,0,-2):
#     print(i)
# 10
# 8
# 6
# 4
# 2

#reversed()返回一个反转后的迭代器
# a = [1,2,3,4,5]
# b = reversed(a)
# print(a,list(b))
# [1, 2, 3, 4, 5] [5, 4, 3, 2, 1]

#sorted() 升序排序
# a =  [1,2,5,4,3]
# b= sorted(a)
# print(a,b)
# [1, 2, 5, 4, 3] [1, 2, 3, 4, 5]

#round()
#返回浮点数的四舍五入值

# a = round(3.545)
# print(a)
# 4

#slice()
#实现切片对象，主要用在切片操作函数里的参数传递。
# m_s=slice(0,10,2)
# print(m_s)
# m_list=[0,1,2,3,4,5,6,7,8,9,10]
# print(m_list[m_s])
# print(m_list[0:10:2])
# slice(0, 10, 2)
# [0, 2, 4, 6, 8]
# [0, 2, 4, 6, 8]

#staticmethod()返回函数的静态方法

#sum()求和
#sum(iterable[, start])
#
# iterable - - 可迭代对象，如：列表、元组、集合。
# start - - 指定相加的参数，如果没有设置这个值，默认为0。
#
# a=sum([1,2,3])
# b=sum([1,2,3],1)
# c=sum([1,2,3],2)
# print(a,b,c)
# 6 7 8

#zip()
#用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
# 然后返回由这些元组组成的列表。
#如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，
# 利用 * 号操作符，可以将元组解压为列表,
# a= [1,2,3]
# b= [4,5,6,7]
# c=list(zip(a,b))
# d=list(zip(*zip(a,b))) #返回一个矩阵
# print(c)
# print(d)
#
# [(1, 4), (2, 5), (3, 6)]
# [(1, 2, 3), (4, 5, 6)]

# __import__()
# 函数用于动态加载类和函数 。
# 如果一个模块经常变化就可以使用 __import__() 来动态载入。
# import sys
# __import__('a')        # 导入 a.py 模块