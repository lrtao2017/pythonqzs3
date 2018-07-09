#!/usr/bin/env python
__author__ = "lrtao2010"

#Python 3.7.0 字典常用方法

#字典的key是唯一的，且不能被修改，value可以是任意值
#字典是无序的

# info = {'name':'tom','age':'10'}
#
# info1 = {
#     'name':'tom',
#     'age':'10'
# }

# info = {'name':'tom','age':'10'}
# v1 = info['name']
# v2 = info['age']
#
# print(v1,v2)
# tom 10

# info = {
#     'name':[
#         11,
#         22,
#         33,
#         {
#             'here':'ok'
#         }
#
#     ]
# }
#
# v = info['name'][3]['here']
# print(v)
# ok







##################################################################

#删除k,v
# info = {'name':'tom','age':'10'}
# del info['age']
# print(info)
# {'name': 'tom'}