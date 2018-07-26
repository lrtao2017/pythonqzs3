#!/usr/bin/env python 
__author__ = "lrtao2010" 

import login
login_ok = ''

goods_code = {
    '0001':{'电脑':'1999'},
    '0002':{'鼠标':'10'},
    '0003':{'游艇':'20'},
    '0004':{'美女':'998'}
}
def shopping():
    print('%-6s %-6s %s ' % ("商品编号","商品名称","商品价格"))
    for k in goods_code.keys():
        for k2,v2 in goods_code[k].items():
            print('{:^8}'.format(k),'{:^10}'.format(k2),'{:^8}'.format(v2))

if __name__ == '__main__':
    login.login()
    if login_ok == 'ok':
        shopping()