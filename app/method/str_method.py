#!/usr/bin/env python
#Python 3.7.0 字符串常用方法
__author__ = "lrtao2010"

#capitalize 将字符串的首字符改为大写
# a = "lrtao"
# v = a.capitalize()
# print(v)
# Lrtao

#casefold 将字符串所有字符改为小写，功能强大
# a = "LrTao"
# v = a.casefold()
# print(v)
# lrtao

#lower 将字符串所有字符改为小写
# a = "LrTao"
# v = a.lower()
# print(v)
# lrtao

#upper 将字符全部转成大写
# a = "LrTao"
# v = a.upper()
# print(v)
# LRTAO

#center(self, width, fillchar=None) 内容居中，width：总长度（当width<len(s)时没有效果）；
#                                   fillchar：空白处填充内容，默认无
# a = "lrtao"
# v = a.center(20,'*')
# print(v)
# *******lrtao********

#ljust(self, width: int, fillchar: str = ...)内容左对齐，右侧填充,不指定默认空白
# a = "lrtao"
# v1 = a.ljust(20,'*')
# v2 = a.ljust(20)
# print(v1)
# print(v2)
# lrtao***************
# lrtao

#rjust(self, width: int, fillchar: str = ...)内容右对齐，左侧填充,不指定默认空白
# a = "lrtao"
# v1 = a.rjust(20,'*')
# v2 = a.rjust(20)
# print(v1)
# print(v2)
# ***************lrtao
#                lrtao

# zfill(self, width: int) z指zero，用0将字符填充到指定长度(左侧填充)
# a = "example"
# v = a.zfill(20)
# print(v)
# 0000000000000000test

# a = "example"
# v1 = a.rjust(20,'0')
# print(v1)
# 0000000000000000test

#count(self, sub, start=None, end=None) 统计子序列在字符串里出现的次数,包括start，不包括end

# a = "lilelili"
# v1 = a.count('li')
# v2 = a.count('li',1)
# v3 = a.count('li',1,6)
# print(v1,v2,v3)
# 3 2 1
#encode(encoding='utf-8',errors='strict')  以encoding指定的编码格式对字符串进行编码
# a = "lilei"
# v = a.encode(encoding='utf-8')
# print(v)
# b'lilei'
#

#endswith(self, suffix, start=None, end=None)是否以指定字符串结束,返回值为布尔值

# a = "hello"
# v1 = a.endswith('o')
# v2 = a.endswith('l')
# v3 = a.endswith('lo')
# v4 = a.endswith('e',0,2)

# print(v1,v2,v3,v4)
# True False True True

#startswith(self, prefix: Union[str, Tuple[str, ...]], start: Optional[int] = ...,end: Optional[int] = ...)
#是否以指定字符串开始,返回值为布尔值
# a = "hello"
# v1 = a.startswith('h')
# v2 = a.startswith('e')
# v3 = a.startswith('he')
# v4 = a.startswith('e',1,3)
#
# print(v1,v2,v3,v4)
# True False True True

#expandtabs
# 按指定的宽度对字符串进行分割，遇到tab字符（\t）转化为空格，默认以8个字符位置分割
#可用作格式化
# a = '1234\t56\t7890\t0\t123'
# v = a.expandtabs(6)
# u_e_p = 'username\temail\tpasswd\nlrtao2010\tlrtao2010@163.com\t123456\nlrtao\tlrtao@163.com\t123'
# v1 = u_e_p.expandtabs(30)
# print(v)
# print(v1)
# 1234  56    7890  0     123
# username                      email                         passwd
# lrtao2010                     lrtao2010@163.com             123456
# lrtao                         lrtao@163.com                 123

# find(self, sub, start=None, end=None) 返回首次找到子序列的位置，如果没找到，返回 -1
# a = 'lilei'
# v1 = a.find('l')
# v2 = a.find('l',2)
# v3 = a.find('lei',2,4)
# print(v1,v2,v3)
# 0 2 -1

#index(self, sub, start=None, end=None)返回首次找到子序列的位置，如果没找到程序会报异常
# a = 'lilei'
# v = a.index('ll')
# print(v)
# Traceback (most recent call last):
#     v = a.index('ll')
# ValueError: substring not found

#rfind(self, sub: str, __start: Optional[int] = ..., __end: Optional[int] = ...)
#返回指定子串的最大索引，如果没找到则返回-1，可以指定要开始和结束位置。
# a = 'lilililili'
# v1 = a.rfind('li')
# v2 = a.rfind('li',9)
# v3 = a.rfind('li',2,4)
# print(v1,v2,v3)
# 8 -1 2

#rindex(self, sub: str, __start: Optional[int] = ..., __end: Optional[int] = ...)
#返回指定子串的最大索引，如果没找到则抛异常，可以指定要开始和结束位置。
# a = 'lilililili'
# v1 = a.rindex('li')
# v2 = a.rindex('li',9)
# v3 = a.rindex('li',2,4)
# print(v1)
# print(v2)
# print(v3)
# v2 = a.rindex('li',9)
# ValueError: substring not found
#
# Process finished with exit code 1


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


#isidentifier 判断字符串是否包含python的保留字
# v1 = 'def'.isidentifier()
# v2 = 'aaa'.isdecimal()
# print(v1,v2)
# True False

#islower 字符串中不能出现大写字母，并且至少有一个小写字母
# a = 'ls12#3'
# b = 'Ls'
# c = '1234s'
# d = 'LS'
# v1 = a.islower()
# v2 = b.islower()
# v3 = c.islower()
# v4 = d.islower()
# print(v1,v2,v3,v4)
# True False True False

#isprintable 检查字符串中是否包含不可安原型显示的内容
# a = 'example'
# b = 't\example' #\t在print时不能显示为\t
# c = 'example\n' #\n在print时不能显示为\n
# v1 = a.isprintable()
# v2 = b.isprintable()
# v3 = c.isprintable()
# print(v1,v2,v3)
# True False False


#isspace 判断字符串是否全部是空格
# a = ''
# b = ' '
# c = 'a b'
# v1 = a.isspace()
# v2 = b.isspace()
# v3 = c.isspace()
# print(v1,v2,v3)
# False True False

#title  标题格式(可以理解为单词首字母大写，其它字符小写)
# a = 'this is title'
# v = a.title()
# print(v)
# This Is Title

#istitle 判断是否是标题格式（可以理解为首字母是否大写）
# a = "this is title"
# b = "This is title"
# c = "This Is title"
# d = "This Is Title"
# v1 = a.istitle()
# v2 = b.istitle()
# v3 = c.istitle()
# v4 = d.istitle()
# print(v1,v2,v3,v4)
# False False False True

#isupper 判断字母是否全部是大写
# a = 'lsL123'
# b = 'LSF123'
# c = 'LSF'
# d = 'LS F'
# v1 = a.isupper()
# v2 = b.isupper()
# v3 = c.isupper()
# v4 = d.isupper()
# print(v1,v2,v3,v4)
# False True True True

#join(self, iterable: Iterable[str])返回一个用指定分隔符分隔的字，
#                                   或者是将指定字符加入到另一个字符中。
# a = 'iamtom'
# v1 = '.'.join(a)
# v2 = '#'.join(a)
# print(v1)
# print(v2)
# i.a.m.t.o.m
# i#a#m#t#o#m

#partition(self, sep: str) 按照指定的字符将字符串分为前中后三部分,从左侧开始
# a = "iamtom"
# v1 = a.partition("i")
# v2 = a.partition('am')
# v3 = a.partition('om')
# v4 = a.partition('som')
# print(v1)
# print(v2)
# print(v3)
# print(v4)
# ('', 'i', 'amtom')
# ('i', 'am', 'tom')
# ('iamt', 'om', '')
# ('iamtom', '', '')

#rpartition(self, sep: str) 与partition一样，但是从右边开始
# a = "iamtom"
# v1 = a.rpartition("i")
# v2 = a.rpartition('am')
# v3 = a.rpartition('tom')
# v4 = a.rpartition('som')
# print(v1)
# print(v2)
# print(v3)
# print(v4)
# ('', 'i', 'amtom')
# ('i', 'am', 'tom')
# ('iam', 'tom', '')
# ('', '', 'iamtom')


#replace(self, old: str, new: str, count: int = ...) 替换字符，不指定次数默认全部替换
# a = 'iamtomtomtom'
# v1 = a.replace('m','i')
# v2 = a.replace('m','i',1)
# print(a)
# print(v1)
# print(v2)
# iamtomtomtom
# iaitoitoitoi
# iaitomtomtom



#split(self, sep: Optional[str] = ..., maxsplit: int = ...)
#按指定字符串从左侧开始进行切割，可以指定切割次数(不指定全部切割)

# a = 'iamtomtom'
# v1 = a.split('m')
# v2 = a.split('m',2)
# print(v1)
# print(v2)
# ['ia', 'to', 'to', '']
# ['ia', 'to', 'tom']

#rsplit(self, sep: Optional[str] = ..., maxsplit: int = ...)
#按指定字符串从右侧开始进行切割，可以指定切割次数(不指定全部切割)
# a = 'iamtomtom'
# v1 = a.rsplit('m')
# v2 = a.rsplit('m',2)
# print(v1)
# print(v2)
# ['ia', 'to', 'to', '']
# ['iamto', 'to', '']

#strip(self, chars: Optional[str] = ...)
#移除两侧（最外侧）指定字符串，默认移除空格，以指定多个字符

# a = ' i am tom m'
# v1 = a.strip()
# v2 = a.strip('m')
# v3 = a.strip('ap')
# v4 = a.strip('am')
# print(v1)
# print(v2)
# print(v3)
# print(v4)
# i am tom m
#  i am tom
#  i am tom m
#  i am tom

#rstrip(self, chars: Optional[str] = ...)
#移除右侧指定字符

# a = ' i am tom m'
# v1 = a.rstrip()
# v2 = a.rstrip('m')
# v3 = a.rstrip('ap')
# v4 = a.rstrip('am')
# print(v1)
# print(v2)
# print(v3)
# print(v4)
 # i am tom m
 # i am tom
 # i am tom m
 # i am tom

#lstrip 移除左侧空白
# a = ' i am tom m '
# v1 = a.lstrip()
# print(v1)
# i am tom m


 #splitlines(self, keepends: bool = ...)
 #按换行符\n切割，如果没指定keepends=True，则会将其从结果中移除
# a = "this is test1\n this is test2"
# v1 = a.splitlines(keepends=True)
# v2 = a.splitlines()
# print(v1)
# print(v2)
# ['this is test1\n', ' this is test2']
# ['this is test1', ' this is test2']

#swapcase 大小写转换
# a = 'This Is Test 01'
# v = a.swapcase()
# print(v)
# tHIS iS tEST 01

#translate(self, table: Optional[bytes], delete: bytes = ...)
#translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符,
# 要过滤掉的字符放到 deletechars 参数中

# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)  # 制作翻译表
# str = "this is string example....wow!!!"
# print(str.translate(trantab))
# th3s 3s str3ng 2x1mpl2....w4w!!!

# 制作翻译表
# bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#
# # 转换为大写，并删除字母o
# print(b'runoob'.translate(bytes_tabtrans, b'o'))
# b'RUNB'

################################################################################################
#字符串也有索引的概念
# a = 'index'
# v1 = a[0]
# v2 = a[3]
# v3 = a[-1]
# v4 = a[0:4]
# print(v1,v2,v3,v4)
# i e x inde

#len()
#
# a = 'abc'
# b = '测试'
# v1 = len(a)
# v2 = len(b)
# print(v1,v2)
# 3 2

#对字符串可以直接使用for、while 循环

# a = '测试'
#
# for i in a:
#     print(i)
# 测
# 试
#
# index = 0
# while index < len(a):
#     print(a[index])
#     index += 1
# 测
# 试

