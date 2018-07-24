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

# for city_name in enumerate(menu.keys()):
#     print(city_name[0],city_name[1])
# des_city = int(input("请选择想要去往的省/直辖市(0|1|2): "))
# if des_city == 0:
#     for area_name in enumerate(menu.get("北京")):
#         print(area_name[0],area_name[1])
#     des_area = int(input("请选择想要去往的市区(0|1|2|3): "))
#     if des_area == 0:
#         print(menu.get("北京").get("海淀"))
# elif des_city == 1:
#     print(2)
# else:
#     print(3)

# level =[]
# while True:
#     for key in menu:
#         print(key)
#     your_choice = input("your choice >>:").strip()
#     if your_choice == "b":
#         if len(level) == 0:break  #当列表空的时候，就是退出大循环的时候
#         menu=level[-1]
#         level.pop()  #删除列表最后一个元素，
#         print(level)
#         # break
#     elif your_choice in menu:
#          # print(menu)
#          level.append(menu)
#          # print(level)
#          menu=menu[your_choice]
#     else:
#          continue

# if __name__ == '__main__':
#     current_layer = menu
#     parent_layer = []    #将父级key值放入到列表中
#     flags = False  #设置标志位
#     while not flags:
#         for key in current_layer:
#             print(key)
#         choose = input("请选择，输入b返回上一级菜单，输入q退出菜单:").strip()
#         if choose in current_layer:
#             parent_layer.append(current_layer)   #将当前的状态放入列表中
#             current_layer = current_layer[choose]
#         elif choose == 'b':
#             if parent_layer:
#                 current_layer = parent_layer.pop()
#         elif choose == 'q':
#             flags = True
#         else:
#             print("\033[34;1m输入有误，请重新输入\033[0m")