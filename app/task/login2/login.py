#!/usr/bin/env python
__author__ = "lrtao2010"

name_list = ['zhangsan','李四','wangwu']
passwd_list = ['123456','abc','123abc']

locked_un_file = "lock.txt"

error_count = 0

while error_count < 3:
    user_name = input("请输入用户名：" )
    user_password = input("请输入密码：")

    #检查账号是否被锁定
    with open(locked_un_file,'r') as L:
        for Line in L.readlines():
            Lines = Line.split()
            if user_name == Lines[0]:
                print("%s 账号已经被锁定，请联系管理员解锁账号" % user_name)
                break

    # 从第二次输入开始判断用户名是否和上次一致
    if error_count == 0:
        user_name_old = user_name
    if error_count > 0 and user_name_old != user_name:
        print('请输入第一次输入的用户名')
        continue
    # 验证账号密码
    if user_name in name_list and user_password == passwd_list[name_list.index(user_name)]:
        print("欢迎 %s 登录" % user_name)
        break
    else:
        print("用户名或密码错误")
        error_count += 1
    #相同账号、密码错误三次被锁定
    if error_count == 3:
        with open(locked_un_file, 'a') as user_lock:
            user_lock.write(user_name + '\n')
        print("用户名、密码错误三次，%s 账号已被锁定，请联系管理员解锁账号" % user_name)
