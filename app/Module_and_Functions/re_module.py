#!/usr/bin/env python 
__author__ = "lrtao2010" 

#python3.7 re模块

#元字符
'''
.  匹配任意一个字符，包括.本身
^  开始
$  结尾
*  紧挨着的字符数量[0，∞）最大数量匹配
+  紧挨着的字符数量[1，∞）最大数量匹配
?  紧挨着的字符数量[0，1 ]最小数量配置
{} 指定紧挨着的字符数量
[] 字符集，在字符集里有功能的符号: - (范围),^（非）, \(转义)，其他符合都没有特殊功能
|  指明两项之间的一个选择(‘或’)
() 标记一个子表达式的开始和结束位置
\  转义字符
'''
import re
#str_test = 'adfsdsdse0823sfeweew39we24sdf3afw2q33rd0df323f4t236s'
# print(re.findall('r..d',str_test))
# ['rd0d']
# print(re.findall('^r..d',str_test))
# []
# print(re.findall('t...s$',str_test))
# ['t236s']
# print(re.findall('we',str_test))
# ['we', 'we']
# print(re.findall('we*',str_test))
# ['wee', 'w', 'we', 'w']
# print(re.findall('we+',str_test))
# ['wee', 'we']
# print(re.findall('we?',str_test))
# ['we', 'w', 'we', 'w']
# print(re.findall('we{1,2}',str_test))
# ['wee', 'we']
# print(re.findall('we{2}',str_test))
# ['wee']

#字符集[]
#str_test = 'addsdsdsea08AB23sfeweew39we24sdf3affw2q33rd0df323f4t236s'
# print(re.findall('a[a-z]',str_test))
# ['ad', 'af']
# print(re.findall('a[^a-z]',str_test))
# ['a0']
# print(re.findall('a[a-z]?',str_test))
# ['ad', 'a', 'af']
# print(re.findall('a[a-z]+',str_test))
# ['addsdsdsea', 'affw']
# print(re.findall('a[a-z]*',str_test))
# ['addsdsdsea', 'affw']
# print(re.findall('[0-9]+',str_test))
# ['08', '23', '39', '24', '3', '2', '33', '0', '323', '4', '236']

#转义符\
'''
反斜杠后边跟元字符去除特殊功能,比如\.
反斜杠后边跟普通字符实现特殊功能,比如\d

\d  匹配任何十进制数；它相当于类 [0-9]。
\D 匹配任何非数字字符；它相当于类 [^0-9]。
\s  匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
\S 匹配任何非空白字符；它相当于类 [^\t\n\r\f\v]。
\w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
\W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
\b  匹配一个特殊字符边界，比如空格 ，&，＃等

'''
#str_test = 'addsdsdsea08AB23sfeweew39we24s\df3affw2q33rd0df323f4t236s'
# print(re.findall('[0-9]+',str_test))
# ['08', '23', '39', '24', '3', '2', '33', '0', '323', '4', '236']
# print(re.findall('\d+',str_test))
# ['08', '23', '39', '24', '3', '2', '33', '0', '323', '4', '236']
# print(re.findall('\d',str_test))
# ['0', '8', '2', '3', '3', '9', '2', '4', '3', '2', '3', '3', '0', '3', '2', '3', '4', '2', '3', '6']
# print(re.findall('\\\\d',str_test))
# ['\\d'] #\d
# print(re.findall(r'\\d',str_test))
# ['\\d'] #\d

#()
# str_test = 'we0wewe1wewewe2wewewewe3wewewewewe4wewewewewewe5'
# print(re.findall(r'(we)+',str_test))
# print(re.findall(r'(we){1}',str_test))
# print(re.findall(r'(we){2}',str_test))
# print(re.findall(r'(we){3}',str_test))
# print(re.findall(r'(we){4}',str_test))
# print(re.findall(r'(we){5}',str_test))
# print(re.findall(r'(we){6}',str_test))
# print(re.findall(r'(we){7}',str_test))
# ['we', 'we', 'we', 'we', 'we', 'we']
# ['we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we']
# ['we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we']
# ['we', 'we', 'we', 'we', 'we']
# ['we', 'we', 'we']
# ['we', 'we']
# ['we']
# []

#|
# str_test = 'addsdsdsea08AB23sfeweew39we24s\df3affw2q33rd0df323f4t236s'
# print(re.search('\d+|(df)',str_test).group())
# 08

#re 方法
#findall('a','abc')    #返回所有满足匹配条件的结果,放在列表里
#re.search('a','abcad').group()
#函数会在字符串内查找模式匹配,直到找到第一个匹配然后返回一个包含匹配信息的对象,
#通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
# print(re.findall('a','abcad'))
# print(re.search('a','abcad').group())
# print(re.search('a','abcad'))
# print(re.search('ac','abcad'))
# # ['a', 'a']
# # a
# # <re.Match object; span=(0, 1), match='a'>
# # None
#re.match('a','abc').group()     #同search,不过仅在字符串开始处进行匹配

#re.split('[ab]','abcd')     #先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
# print(re.split('[ab]','abcd'))
# ['', '', 'cd']

#sub 替换
# ret0 = re.sub('\d','A','adae123456adfe') #全部替换
# ret1 = re.sub('\d','A','adae123456adfe',2) #指定替换次数
# ret2 = re.subn('\d','A','adae123456adfe')  #全部替换，并返回替换次数
# ret3 = re.subn('\d+','A','adae123456ad23123f23232e',2)
#
# print(ret0)
# print(ret1)
# print(ret2)
# print(ret3)
#
# # adaeAAAAAAadfe
# # adaeAA3456adfe
# # ('adaeAAAAAAadfe', 6)
# # ('adaeAadAf23232e', 2)

#compile 将规则进行编译，在重复多次执行一个规则时使用
# com_test = re.compile('\d{2}')
# ret0 = com_test.search('abc123ee345')
# ret1 = com_test.findall('abc123ee345')
# print(ret0.group())
# print(ret1)
# # 12
# # ['12', '34']

#finditer 将匹配到的内容生成可迭代对象，在大数据配置时使用
# ret = re.finditer('\d','awe23223ee32dr3523ser')
# print(ret)
#
# print(next(ret).group())
# print(next(ret).group())
# print(next(ret).group())
# print(next(ret).group())
# # <callable_iterator object at 0x00000000025C6438>
# # 2
# # 3
# # 2
# # 2

#匹配优先级

# ret0=re.findall('www\.(baidu|163)\.com','qser223www.baidu.comdfetwww.163.comaewrs')
# ret1=re.findall('www\.(?:baidu|163)\.com','qser223www.baidu.comdfetwww.163.comaewrs') #取消优先级
#
# print(ret0)
# print(ret1)
# # ['baidu', '163']
# # ['www.baidu.com', 'www.163.com']

#匹配所有整数
# ret0=re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
# ret1=re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# ret1.remove("")
#
# print(ret0)
# print(ret1)
# # ['1', '2', '60', '40', '35', '5', '4', '3']
# # ['1', '-2', '60', '5', '-4', '3']

#匹配内容分组
# ret = re.search('(?P<name>[a-zA-Z]+)(?P<age>\d+)','lilie18tom17')
# # print(ret.group('name'))
# # print(ret.group('age'))
# # # lilie
# # # 18

#ret = re.finditer('(?P<name>[a-zA-Z]+)(?P<age>\d+)','lilie18tom17hanmeimei16')
# print(next(ret).group('name','age'))
# print(next(ret).group('name','age'))
# print(next(ret).group('name','age'))
# # ('lilie', '18')
# # ('tom', '17')
# # ('hanmeimei', '16')

#使用for循环
# for i in ret:
#     print(i.group('name','age'))
#
# # ('lilie', '18')
# # ('tom', '17')
# # ('hanmeimei', '16')
