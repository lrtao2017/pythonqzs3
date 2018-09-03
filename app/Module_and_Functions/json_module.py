#!/usr/bin/env python 
__author__ = "lrtao2010" 

#python3.7 json模块

'''
要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
比如XML，但更好的方法是序列化为JSON，
因为JSON表示出来就是一个字符串，可以被所有语言读取，
也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
'''

'''
对象(变量)从内存中变成可存储或传输的过程称之为序列化,
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化。
'''
#json 规则
'''
1、字符串必须用"",单引号报错；
2、无论数据是怎样创建的，只要满足json格式，
   就可以json.loads出来,不一定非要dumps的数据才能loads。
'''

import json

# dic = {'name':'test','age':18}
# json_dic = json.dumps(dic)
# print(json_dic,type(json_dic))
# {"name": "test", "age": 18} <class 'str'>

# dic = '{"name":"test","age":18}'
# json_dic = json.loads(dic)
# print(json_dic,type(json_dic))
# {'name': 'test', 'age': 18} <class 'dict'>

# json_f = 'json_text.txt'
# json_dic = {'name':'test','age':18}
# with open(json_f,'w') as f:
#     f.write(json.dumps(json_dic))  #等同于json.dump(json_dic,f)，dump只能用于写入磁盘。

# with open(json_f) as f:
#     my_dic=json.loads(f.read()) #等同于my_dic=json.load(f)，load只能用于从磁盘读取
#
# print(my_dic['name'])
# test