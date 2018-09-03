#!/usr/bin/env python 
__author__ = "lrtao2010" 

# python3.7 倒计时
import time
for i in range(10,-1,-1):
    print('\r','距离游戏结束还有 %s 秒！' % str(i).zfill(2),end='')
    time.sleep(1)
print('\r','{:^20}'.format('游戏结束！'))
