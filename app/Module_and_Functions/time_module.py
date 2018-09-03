#!/usr/bin/env python 
__author__ = "lrtao2010" 

#python3.7 time模块

#time模块没有time.py文件，是内置到解释器中的模块

#三种时间表示方式
'''
1、时间戳（timestamp）: 通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。
2、格式化的时间字符串："2018-09-03 10:02:01"
3、元组（struct_time）:struct_time元组共有9个元素共九个元素:(年，月，日，时，分，秒，一年中第几周，一年中第几天，夏令时)
'''

import time

#时间戳 time()
# print(time.time())
# 1535939025.4159343

#struct_time
#localtime([secs]) 将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
#当地时间
# print(time.localtime(time.time()))
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=3, tm_hour=9, tm_min=46, tm_sec=7, tm_wday=0, tm_yday=246, tm_isdst=0)
# print(time.localtime()) #
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=3, tm_hour=9, tm_min=48, tm_sec=19, tm_wday=0, tm_yday=246, tm_isdst=0)

# t_local=time.localtime()
# print(t_local.tm_year)
# print(t_local.tm_mon)
# print(t_local.tm_mday)
# 2018
# 9
# 3

#gmtime([secs])  将一个时间戳转换为UTC时区（0时区）的struct_time。
# print(time.gmtime())
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=3, tm_hour=1, tm_min=51, tm_sec=38, tm_wday=0, tm_yday=246, tm_isdst=0)

#mktime(t) : 将一个struct_time转化为时间戳。
# print(time.mktime(time.localtime()))
# 1535939934.0

# asctime([t]) : 把一个表示时间struct_time表示为这种形式：'Mon Sep  3 10:01:46 2018'。
# 默认将time.localtime()作为参数传入。

# print(time.asctime())
# Mon Sep  3 10:01:46 2018

#ctime([secs]) : 把一个时间戳转化为time.asctime()的形式,默认time.time()为参数。
# print(time.ctime())
# Mon Sep  3 10:05:40 2018

#strftime(format[, t])
# 把一个代表时间的struct_time转化为格式化的时间字符串。
# 如果t未指定，将传入time.localtime()。
# 如果元组中任何一个元素越界，ValueError的错误将会被抛出。
# print(time.strftime("%Y-%m-%d %X"))  #%X 等同于 %H%M%S
# print(time.strftime("%Y-%m-%d %X",time.localtime()))
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 2018-09-03 10:14:53
# 2018-09-03 10:14:53
# 2018-09-03 10:14:53

#strptime(string[, format])
# 把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
# print(time.strptime('2018-09-03 10:14:53', '%Y-%m-%d %X'))
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=3, tm_hour=10, tm_min=14, tm_sec=53, tm_wday=0, tm_yday=246, tm_isdst=-1)

#sleep(secs)
#time.sleep(10) #停止10秒，继续运行

# import datetime
# print(datetime.datetime.now())
# 2018-09-03 10:20:50.680030