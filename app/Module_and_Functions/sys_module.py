#!/usr/bin/env python 
__author__ = "lrtao2010" 

#python3.7 sys模块

#sys模块负责程序与python解释器的交互，提供了一系列的函数和变量，
#用于操控python运行时的环境。

# sys.argv 接收命令行参数，生成一个List，第一个元素是程序本身路径
# sys.modules.keys() 返回所有已经导入的模块列表
# sys.exc_info() 获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
# sys.exit(n) 退出程序，正常退出时exit(0)
# sys.hexversion 获取Python解释程序的版本值，16进制格式如：0x020403F0
# sys.version 获取Python解释程序的版本信息
# sys.maxint 最大的Int值
# sys.maxunicode 最大的Unicode值
# sys.modules 返回系统导入的模块字段，key是模块名，value是模块
# sys.path 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform 返回操作系统平台名称
# sys.stdout 标准输出
# sys.stdin 标准输入
# sys.stderr 错误输出
# sys.exc_clear() 用来清除当前线程所出现的当前的或最近的错误信息
# sys.exec_prefix 返回平台独立的python文件安装的位置
# sys.byteorder 本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'
# sys.copyright 记录python版权相关的东西
# sys.api_version 解释器的C的API版本

# import sys
# my_sys = sys.argv
# for i in my_sys:
#     print(i)
# >>>python sys_module.py example test1 test2
# sys_module.py
# example
# test1
# test2
# print(sys.path)

# print(__name__)
# print(__file__)
#
# __main__
# sys_module.py


#import sys,os
# print(os.path.abspath(__file__))
# E:\python\learning\app\Module_and_Functions\sys_module.py
#print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from method import example
# example.example()
# ModuleNotFoundError: No module named 'method'

#动态修改sys.path变量
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# from method import example
# example.example()
#
# This is example

#实时打印输出
#显示进度条
# import time,sys
# for i in range(20):
#     sys.stdout.write("=")
#     time.sleep(0.5)
#     sys.stdout.flush() #从缓存刷新的屏幕

#显示百分比
# import sys
# import time
#
# def view_bar(num,total):
#     rate = int(float(num) * 100 / float(total))
#     r = '\r%d%%' % (rate,) #\r 光标退格到行首
#     sys.stdout.write(r)
#     sys.stdout.flush()
#
# if __name__ == '__main__':
#     for i in range(0,101):
#         view_bar(i,100)
#         time.sleep(0.3)

#显示进度条+百分比
# import sys
# import time
#
# def view_bar(num,total):
#     rate = int(float(num) * 100 / float(total))
#     progress_bar = '{:<55}'.format('=' * int(num / 2))
#     percent_ratio = '{:>5}'.format('%s%%' % (rate,))
#     sys.stdout.write('\r'+ progress_bar + percent_ratio)
#     sys.stdout.flush()
#
# if __name__ == '__main__':
#     for i in range(0,101):
#         view_bar(i,100)
#         time.sleep(0.3)