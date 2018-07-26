#!/usr/bin/env python 
__author__ = "lrtao2010" 

import login,sys

error_input_count = 0
shopping_list = {}

goods_code = {
    '0001':{'电脑':1999 },
    '0002':{'鼠标':10 },
    '0003':{'游艇':20 },
    '0004':{'美女':998 }
}
def shopping():
    print('\n')
    bc_balance_in = input("请输入您的银行卡余额(元)：").strip()
    if bc_balance_in.isdigit():
        bc_balance = int(bc_balance_in)
    else:
        print("\033[1;33m输入有误\033[0m")
        global error_input_count
        error_input_count += 1
        if error_input_count == 3:
            print("\033[1;31m此次购物很不愉快，再见！\033[0m")
            sys.exit()
        else:
            shopping()
    print('\n商品明细表如下：')
    print('%-6s %-6s %s ' % ("商品编号","商品名称","商品价格"))
    for k in goods_code.keys():
        for k2,v2 in goods_code[k].items():
            print('{:^8}'.format(k),'{:^11}'.format(k2),v2)

    continue_to_buy = 'Y'
    while continue_to_buy == 'Y':
        if bc_balance < 10:
            print('卡上余额严重不足，今天购物到此结束')
            continue_to_buy = 'N'
            continue
        product_number = input('请输入您要购买商品的商品编号（每次限购一种）').strip()
        if product_number in goods_code.keys():
            amount = input('请输入购买数量:').strip()
            if amount.isdigit():
                amount = int(amount)
                for k,v in goods_code[product_number].items():
                    goods_name = k
                    goods_price = v

                t_price = amount * goods_price #计算购买商品总价
                if bc_balance >= t_price:
                    #加入购物车
                    bc_balance -= t_price
                    print('现在卡上余额为 %s 元' % bc_balance )
                    if goods_name in shopping_list.keys():
                        shopping_list[goods_name] += amount
                    else:
                        shopping_list.update({goods_name:amount})
                else:
                    print('卡上余额不足,请重新选择商品和数量')

            else:
                print('\033[1;33m输入有误，请重新购买\033[0m')
        else:
            print('\033[1;33m输入有误，请重新购买\033[0m')

if __name__ == '__main__':
    # if login.login() == "ok":
    #    shopping()
    shopping()