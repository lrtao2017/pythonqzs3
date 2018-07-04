#!/usr/bin/env python
__author__ = "lrtao2010"

#Fenshu = input("请输入你的分数：")
Fenshu = int(input("请输入你的总分数："))
Fenshu_yw = int(input("请输入你的语文分数："))
if Fenshu >= 180:
    if Fenshu_yw >= 95:
        print('A+')
    else:
        print('A')
elif Fenshu >= 160:
    print('B')
elif Fenshu >= 140:
    print('C')
elif Fenshu >= 120:
    print('D')
else:
    print('E')