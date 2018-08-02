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
#将整数转换为前缀为“0b”的二进制字符串。
# 结果是一个有效的Python表达式。
# 如果x不是Python int对象，则必须定义一个返回整数的__index __（）方法。

# a = bin(3)
# b = bin(-3)
# print(a,b)
# 0b11 -0b11

#class bool([x])
#返回一个布尔值，即True或False之一。
# 使用标准真值测试程序转换x。 如果x为false或省略，则返回False; 否则返回True
# a = bool(0)
# b = bool(1)
# c = bool(-1)
# d = bool("")
# print(a,b,c,d)
# False True True False

