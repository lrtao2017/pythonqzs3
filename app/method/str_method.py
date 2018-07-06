#!/usr/bin/env python
#Python 3 字符串常用方法
__author__ = "lrtao2010"

#capitalize 首字母大写
# a = "lrtao"
# v = a.capitalize()
# print(v)
# Lrtao

#casefold 全部变小写
# a = "LrTao"
# v = a.casefold()
# print(v)
# lrtao

#center(self, width, fillchar=None) 内容居中，width：总长度；fillchar：空白处填充内容，默认无
# a = "lrtao"
# v = a.center(20,'*')
# print(v)
# *******lrtao********

#count(self, sub, start=None, end=None) 统计子序列个数,包括start，不包括end

# a = "lilelili"
# v1 = a.count('li')
# v2 = a.count('li',1)
# v3 = a.count('li',1,6)
# print(v1,v2,v3)
# 3 2 1
#encode  编码
#

#endswith(self, suffix, start=None, end=None)是否以指定字符串结束,返回值为布尔值

# a = "hello"
# v1 = a.endswith('o')
# v2 = a.endswith('l')
# v3 = a.endswith('lo')
# v4 = a.endswith('e',0,2)

# print(v1,v2,v3,v4)
# True False True True

#expandtabs  将tab转换成空格，如果tab转换空格数量没有定义，默认一个tab转换成8个空格

# find(self, sub, start=None, end=None) 返回首次找到子序列的位置，如果没找到，返回 -1
# a = 'lilei'
# v1 = a.find('l')
# v2 = a.find('l',2)
# v3 = a.find('lei',2,4)
# print(v1,v2,v3)
# 0 2 -1

#index(self, sub, start=None, end=None)返回首次找到子序列的位置，如果没找到程序会报错
# a = 'lilei'
# v = a.index('ll')
# print(v)
# Traceback (most recent call last):
#   File "D:/python3/app/method/str_method.py", line 58, in <module>
#     v = a.index('ll')
# ValueError: substring not found

#format 字符串格式化
# a = 'hello ,{name}!hello ,{name2} !'
# v = a.format(name='lilei',name2='tom')
# print(v)
# hello ,lilei!hello ,tom !

# a = 'hello,{0}! hello,{1}!'
# v = a.format('lilei','tom')
# print(v)
# hello,lilei! hello,tom!

#format_map(self, mapping) 和format相似，参数为字典形式
# a = 'hello ,{name}!hello ,{name2} !'
# v = a.format_map({'name2':'lilei','name':'tom'})
# print(v)
# hello ,tom!hello ,lilei !

#isalnum 是否只包含字母或数字,返回值为布尔值
# a = 'lsL123'
# b = 'ls'
# c = 'LS'
# d = '123'
# e = 'ls@'
# v1 = a.isalnum()
# v2 = b.isalnum()
# v3 = c.isalnum()
# v4 = d.isalnum()
# v5 = e.isalnum()
# print(v1,v2,v3,v4,v5)
# True True True True False

#isalpha 字符串是否全部是字母
# a = 'lsL123'
# b = 'ls'
# c = 'LS'
# d = 'Ls'
# e = 'ls@'
# v1 = a.isalpha()
# v2 = b.isalpha()
# v3 = c.isalpha()
# v4 = d.isalpha()
# v5 = e.isalpha()
# print(v1,v2,v3,v4,v5)
# False True True True False

#isascii Return True if all characters in the string are ASCII, False otherwise.
# a = '12ls er$%^&*()'
# b = '中'
# v1 = a.isascii()
# v2 = b.isascii()
# print(v1,v2)
# True False

#isdecimal 字符串是否是十进制字符串
# a = '1234567890'
# b = 'A0'
# v1 = a.isdecimal()
# v2 = b.isdecimal()
# print(v1,v2)
# True False

#isdigit 如果字符串是数字字符串，则返回True，否则返回False。
# isdecimal() 如果字符串是数字字符串，则返回True，否则返回False。
#isnumeric 如果字符串是数字字符串，则返回True，否则返回False

# num = "一"
# v1 = num.isdigit()
# v2 = num.isdecimal()
# v3 = num.isnumeric()
# print(v1,v2,v3)
# False False True

# num = "Ⅰ" #罗马数字1
# v1 = num.isdigit()
# v2 = num.isdecimal()
# v3 = num.isnumeric()
# print(v1,v2,v3)
# False False True

# num = "1"
# v1 = num.isdigit()
# v2 = num.isdecimal()
# v3 = num.isnumeric()
# print(v1,v2,v3)
# True True True

# isdigit()
# True: Unicode数字,byte数字（单字节）,全角数字（双字节）,罗马数字
# False: 汉字数字
# Error: 无
# isdecimal()
# True: Unicode数字,全角数字（双字节）
# False: 罗马数字,汉字数字
# Error: byte数字（单字节）
# isnumeric()
# True: Unicode数字,全角数字（双字节）,罗马数字,汉字数字
# False: 无
# Error: byte数字（单字节）


#isidentifier 如果字符串是有效的Python标识符，则返回True，否则返回False
# a = '_123'
# b = '123'
# c = 'a123'
# d = '#123'
# v1 = a.isidentifier()
# v2 = b.isidentifier()
# v3 = c.isidentifier()
# v4 = d.isidentifier()
# print(v1,v2,v3,v4)
# True False True False

#islower 字符串中不能出现大写字母，并且至少有一个小写字母
# a = 'ls12#3'
# b = 'Ls'
# c = '1234s'
# d = '1234'
# v1 = a.islower()
# v2 = b.islower()
# v3 = c.islower()
# v4 = d.islower()
# print(v1,v2,v3,v4)
# True False True False

