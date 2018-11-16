#!/usr/bin/env python
__author__ = "lrtao2010"



'''
处理访问日志，筛选时间大于1秒的请求
'''
def api():
    with open('api.log','a+',encoding='utf-8') as f_a:
        with open('wkxz-api.access.log') as f:
            for line in f.readlines():
                if line[-2:] == "-\n" :
                    num =float(line[-7:-2])
                else:
                    num=float(line[-6:])
                if num >= 1.000 :
                    f_a.write(line)


def dz():
    with open('dz.log','a+',encoding='utf-8') as f_a:
        with open('dz.access.log') as f:
            for line in f.readlines():
                if line[-2:] == "-\n":
                    num =float(line[-7:-2])
                else:
                    num=float(line[-6:])
                if num >= 1.000 :
                    f_a.write(line)

if __name__ == '__main__':
    api()
    dz()
