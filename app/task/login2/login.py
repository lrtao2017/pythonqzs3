#!/usr/bin/env python
__author__ = "lrtao2010"

name_list = ['zhangsan','lisi','wangwu']
passwd_list = ['123456','abc','123abc']
locked_account_file = "lock.txt"
error_count = 0
user_lock = 0

while error_count < 3:
    user_name = input("请输入用户名：" ).lower()
    user_password = input("请输入密码：")

    if error_count == 0:
        # 检查账号是否被锁定
        with open(locked_account_file, 'r') as L:
            for Line in L.readlines():
                Lines = Line.split()
                if Lines != [] and user_name == Lines[0]:
                    #!=[]防止locked_account_file中有空行报错
                    print("%s 账号已经被锁定，请联系管理员解锁账号" % user_name)
                    user_lock = 1
                    error_count = 3
                    break
        user_name_old = user_name

    if user_lock == 0:
        # 从第二次输入开始判断用户名是否和上次一致
        if error_count > 0 and user_name_old != user_name:
            print('请输入第一次输入的用户名')
            continue

        # 验证账号密码
        if user_name in name_list:
            if user_password == passwd_list[name_list.index(user_name)]:
                print("欢迎 %s 登录" % user_name)
                break
            else:
                print("用户名或密码错误")
                error_count += 1
                left_count = 3 - error_count
                print('您还有 %s 次重试机会'  % left_count)
                # 存在的账号密码错误三次被锁定
                if error_count == 3:
                    with open(locked_account_file, 'a') as user_lock:
                        user_lock.write(user_name + '\n')
                    print("用户名、密码错误三次，%s 账号已被锁定，请联系管理员解锁账号" % user_name)
        else:
            print("用户名或密码有问题，请联系管理员处理")
            break
