#!/usr/bin/env python 
__author__ = "lrtao2010" 

#数据结构：
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

des_name_dict = menu
key_list = []
no_quit = True
while no_quit:
    for key in des_name_dict.keys():
        print(key) 
    des_name = input("\n请选择目的地(按'b'返回上一层，'q'退出程序)").strip()
    if not des_name:continue
    elif des_name in des_name_dict.keys():
        key_list.append(des_name)
        #print(key_list)
        des_name_dict = des_name_dict[des_name]
        if des_name_dict == {}:
            print("\n已到达最底层，请返回上一层\n")
        continue
    elif des_name == 'b':
        if len(key_list) == 0:
            des_name_dict = menu
            continue
        elif len(key_list) == 1:
            key_list.pop()
            des_name_dict = menu
            continue
        elif len(key_list) == 2:
            key_list.pop()
            des_name_dict = menu[key_list[0]]
            continue
        elif len(key_list) == 3:
            key_list.pop()
            des_name_dict = menu[key_list[0]][key_list[1]]
            continue
    elif des_name == 'q':
        no_quit = False
    else:
        print("输入有误，请重新选择")
        continue


