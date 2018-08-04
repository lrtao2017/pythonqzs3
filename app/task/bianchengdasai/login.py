#!/usr/bin/env python
__author__ = "lrtao2010"

import sys
def login():
    name_passwd = {
        'alex': ['alex123','管理员'],
        'pizza': ['pizza123','教师'],
        'john': ['john123','学生']
    }
    locked_account_file = "lock.txt"
    error_count = 0

    while error_count < 3:
        user_name = input("请输入用户名：" ).strip().lower()
        user_password = input("请输入密码：")

        if error_count == 0:
            # 检查账号是否被锁定
            with open(locked_account_file, 'r') as L:
                for Line in L.readlines():
                    Lines = Line.split()
                    if Lines != [] and user_name == Lines[0]:
                        #!=[]防止locked_account_file中有空行报错
                        print("%s 账号已经被锁定，请联系管理员解锁账号" % user_name)
                        sys.exit()

            user_name_old = user_name

        # 从第二次输入开始判断用户名是否和上次一致
        if error_count > 0 and user_name_old != user_name:
            print('请输入第一次输入的用户名')
            continue

        # 验证账号密码
        if user_name in name_passwd.keys():
            if user_password == name_passwd[user_name][0]:
                print('\033[1;36m%s %s 您好，欢迎光临!\033[0m' % (name_passwd[user_name][1],user_name))
                return user_name,name_passwd[user_name][1]
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
                    sys.exit()
        else:
            print("用户名或密码有问题，请联系管理员处理")
            sys.exit()

if __name__ == '__main__':
    login()