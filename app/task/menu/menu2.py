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
key_list = []   #存放选择的目的地，用于返回上一次
no_quit = True

while no_quit:
    #print(key_list)
    for key in des_name_dict.keys():
        print(key) 
    des_name = input("请选择目的地(按'b'返回上一层，'q'退出程序)>>>").strip()
    if des_name in des_name_dict.keys():
        key_list.append(des_name)
        des_name_dict = des_name_dict[des_name]  #用目的地作为键查找的新字典重置原来的字典
        if len(des_name_dict) == 0:
            print("已到达最底层，请返回上一层")
        continue
    elif des_name == 'b':
        if len(key_list) == 0:
            des_name_dict = menu
            continue
        else:
            key_list.pop()
            if len(key_list) == 0:
                des_name_dict = menu
                continue
            for keys in range(len(key_list)):
                if keys == 0:
                    des_name_dict_old = menu
                des_name_dict = des_name_dict_old[key_list[keys]]   #通过目的地列表重置字典
                des_name_dict_old = des_name_dict
            continue
    elif des_name == 'q':
        no_quit = False
    else:
        print("***输入有误，请重新选择***")
        continue