#!/usr/bin/env python

__author__ = "lrtao2010" 

import login,sys,os

error_input_count = 0
shopping_list = {} #购物车

goods_code = {
    '0001':{'电脑':1999 },
    '0002':{'鼠标':10 },
    '0003':{'游艇':20 },
    '0004':{'美女':998 }
}

def shopping():
    bc_balance_in = input("\033[1;34m请输入您的购物卡余额(元)：\033[0m").strip()
    if bc_balance_in.isdigit():
        bc_balance = int(bc_balance_in)
        bc_balance_z = int(bc_balance_in) #记录卡上原始金额，在购买小票中使用
        print('您的卡上余额为：\033[1;34m%s 元\033[0m,祝您购物愉快！' % bc_balance )
    else:
        print("\033[1;33m输入有误\033[0m")
        global error_input_count
        error_input_count += 1
        if error_input_count == 3:
            print("\033[1;31m卡上没有余额，今天购物到此结束,欢迎下次光临\033[0m")#打印红色字体
            sys.exc_info()
        else:
            shopping()
    print_ex_record = input('\033[1;34m是否查看上次的消费记录y/n（n）:\033[0m').strip()
    if print_ex_record == 'y':
        record_file = "%s_ex_record.txt" % user_name
        if os.path.isfile(record_file):
            with open(record_file, 'r', encoding='utf-8') as L:
                print('\033[1;36m您上次消费信息如下：\033[0m')
                print('\033[1;35m************************\033[0m')
                for line in L.readlines():
                    print(line.rstrip())
                print('\033[1;35m************************\033[0m')
        else:
            print("\033[1;31m没有找到您的消费记录,请继续购物，谢谢合作！\033[0m")
            print('\033[1;35m************************\033[0m')

    print('\n\033[1;36m您可以购买的商品有：\033[0m')
    print('%-6s %-6s %s ' % ("商品编号","商品名称","商品价格"))
    for k in goods_code.keys():
        for k2,v2 in goods_code[k].items():
            print('{:^8}'.format(k),'{:^11}'.format(k2),v2)

    continue_to_buy = 'Y'
    while continue_to_buy == 'Y':
        if bc_balance < 10:
            print('\n\033[1;31m现在卡上余额为 %s 元，余额严重不足，今天购物到此结束,欢迎下次光临!\033[0m' % bc_balance)
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
                    bc_balance -= t_price
                    print('\033[1;34m现在卡上余额为 %s 元，"%s" 已加入购物车\033' % (bc_balance,goods_name) )#打印蓝色字体
                    # 将商品编号和数量加入购物车,
                    if product_number in shopping_list.keys():
                        shopping_list[product_number] += amount
                    else:
                        shopping_list.update({product_number:amount})
                else:
                    print('\033[1;33m现在卡上余额为 %s 元，余额不足\033[0m' % bc_balance)#打印黄色字体
                #是否继续购物，只有输入N/n时，才停止购物
                continue_to_buy_input = input('是否继续购物 Y/N(Y):').strip()
                if continue_to_buy_input == 'N' or continue_to_buy_input == 'n':
                    print('\033[1;32m购物到此结束,欢迎再次光临\033[0m')
                    continue_to_buy = 'N'
            else:
                print('\033[1;33m输入有误，请重新购买\033[0m')
        else:
            print('\033[1;33m输入有误，请重新购买\033[0m')
    #打印购物小票并保存到文件
    if continue_to_buy == 'N':
        if len(shopping_list) == 0:
            print('\n\033[1;36m您今天没有购买任何商品,欢迎下次光临\033[0m')#青蓝色
        else:
            print('\n\033[1;36m购物信息详情:\033[0m')
            record_file = "%s_ex_record.txt" % user_name
            with open(record_file, 'w', encoding='utf-8') as f:
                print('==========================')
                print('==========================', file=f)
                print('%-6s%-6s%s ' % ("商品名称", "商品数量","金  额"))
                print('%-6s%-6s%s ' % ("商品名称", "商品数量", "金  额"), file=f)
                #goods_c 商品编号，goods_a 购买数量，googs_n 商品名称，goods_p 商品单价
                for goods_c,goods_a in shopping_list.items():
                    for goods_n,goods_p in goods_code[goods_c].items():
                        print('{:^7}'.format(goods_n), '{:<9}'.format(goods_a), goods_p * goods_a)
                        print('{:^7}'.format(goods_n), '{:<9}'.format(goods_a), goods_p * goods_a, file=f)
                print('--------------------------')
                print('--------------------------',file=f)
                print('%-8s%s' % ('消费金额总计：',(bc_balance_z - bc_balance)))
                print('%-8s%s' % ('消费金额总计：', (bc_balance_z - bc_balance)),file=f)
                print('%-9s%s' % ('购物卡余额：',bc_balance ))
                print('%-9s%s' % ('购物卡余额：', bc_balance),file=f)
                print('==========================')
                print('==========================',file=f)


#启动购物程序
if __name__ == '__main__':
    user_name = login.login()
    if user_name != '':
        shopping()
