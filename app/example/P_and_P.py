#!/usr/bin/env python 
__author__ = "lrtao2010" 

#python3.7 实时显示进度条和百分比

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
import sys
import time

def view_bar(num,total):
    rate = int(float(num) * 100 / float(total))
    progress_bar = '{:<55}'.format('=' * int(num / 2))
    percent_ratio = '{:>5}'.format('%s%%' % (rate,))
    sys.stdout.write('\r'+ progress_bar + percent_ratio)
    sys.stdout.flush()

if __name__ == '__main__':
    for i in range(0,101):
        view_bar(i,100)
        time.sleep(0.3)