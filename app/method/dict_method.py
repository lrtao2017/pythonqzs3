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

#clear(self) 清空字典
# info = {"name":"tom"}
# info.clear()
# print(info)

#copy(self) 浅复制
# info1 = {"name":['tom']}
# info2 = info1.copy()
# print(info2)
# info1["name"][0] = 'lilei'
# print(info1)
# print(info2)
# {'name': ['tom']}
# {'name': ['lilei']}
# {'name': ['lilei']}

#深复制
# import copy
# info1 = {"name":['tom']}
# info2 = copy.deepcopy(info1)
# print(info2)
# info1["name"][0] = 'lilei'
# print(info1)
# print(info2)
# {'name': ['tom']}
# {'name': ['lilei']}
# {'name': ['tom']}

#fromkeys(*args, **kwargs)使用给定的键建立字典，默认对应值为None
# keys_in = ('name','age')
# keys_out1 = dict.fromkeys(keys_in)
# keys_out2 = dict.fromkeys(keys_in,10)
# print(keys_out1)
# print(keys_out2)
# {'name': None, 'age': None}
# {'name': 10, 'age': 10}

#get(self, *args, **kwargs) 返回指定键的值，如果键不存在，返回默认值
# info1 = {"name":['tom']}
# print(info1.get('name','No'))
# print(info1.get('name1','No'))
# ['tom']
# No

# v = info1['name1'] #键不存在会报异常
# print(v)
#     v = info1['name1']
# KeyError: 'name1'

#items(self) 遍历键值对
# info1 = {"name":['tom']}
# v = info1.items()
# print(v)
# dict_items([('name', ['tom'])])

#keys(self) 遍历键
# info1 = {"name":['tom']}
# v1 = info1.keys()
# print(v1)
# dict_keys(['name'])

#values(self) 遍历值
# info1 = {"name":['tom']}
# v2 = info1.values()
# print(v2)
# dict_values([['tom']])

# info1 = {"name":['tom'],'age':'18','city':'BJ'}
#
# for k,v in info1.items():
#     print("items()",k,v)
# for k1 in info1.keys():
#     print('keys()',k1)
# for v1 in info1.values():
#     print("values()",v1)
# items() name ['tom']
# items() age 18
# items() city BJ
# keys() name
# keys() age
# keys() city
# values() ['tom']
# values() 18
# values() BJ


#pop(self, k, d=None)
# 删除指定的键，并返回值，要是键不存在，并且没有给定d值，报异常，给定d值，返回d值
# info1 = {"name":['tom'],'age':'18'}
# v = info1.pop('name')
# print(v)
# print(info1)
# ['tom']
# {'age': '18'}

# info1 = {"name":['tom'],'age':'18'}
# v = info1.pop('name1')
# print(v)
# print(info1)
#     v = info1.pop('name1')
# KeyError: 'name1'

# info1 = {"name":['tom'],'age':'18'}
# v = info1.pop('name1','Not find')
# print(v)
# print(info1)
# Not find
# {'name': ['tom'], 'age': '18'}

#popitem(self) 随机删除一个，并返回键值对

# info1 = {"name":['tom'],'age':'18','city':'BJ'}
# v = info1.popitem()
# print(v)
# print(info1)
#
# ('city', 'BJ')
# {'name': ['tom'], 'age': '18'}



#setdefault(self, *args, **kwargs)
#向字典中添加键值，如果添加的键在字典中不存在，直接加入键值，默认值为None
# 键存在，则返回对应的值
# info1 = {"name":['tom']}
# v1 = info1.setdefault('name','lei')
# v2 = info1.setdefault('city')
# v3 = info1.setdefault('age','18')
# print(v1)
# print(v2)
# print(v3)
# print(info1)
# ['tom']
# None
# 18
# {'name': ['tom'], 'city': None, 'age': '18'}


#update(self, E=None, **F) 将字典2中的键值对更新到字典1中，要是有重复的键，将被覆盖
# info1 = {'name': ['tom'],'age': '18'}
# info2 = {'name': ['lilei'], 'city': 'BJ'}
# info1.update(info2)
# print(info1)
# print(info2)
# {'name': ['lilei'], 'age': '18', 'city': 'BJ'}
# {'name': ['lilei'], 'city': 'BJ'}

# info1 = {'name': ['tom'],'age': '18'}
# info1.update(name=123,city='SH')
# print(info1)
# {'name': 123, 'age': '18', 'city': 'SH'}
#


##################################################################

#删除k,v
# info = {'name':'tom','age':'10'}
# del info['age']
# print(info)
# {'name': 'tom'}