#!/usr/bin/env python
# --*-- coding=utf-8 --*--
__author__ = "lrtao2010"

'用户登录系统，添加md5加密和验证码功能'

import random, sys, hashlib, re

account_file = 'account.txt'
lock_name_file = 'lock.txt'

login_times = 0


# 生成验证码
def Verification_code():
    V_code_list = []
    for i in range(6):
        v = random.randint(0, 5)
        if 0 <= v <= 1:
            V_code_list.append(chr(random.randint(49, 57)))
        elif 2 <= v <= 3:
            V_code_list.append(chr(random.randint(65, 78)))
        else:
            V_code_list.append(chr(random.randint(97, 107)))
    return ''.join(V_code_list)


# 生成MD5加密密码
def Md5_code(passwd):
    md5_hash = hashlib.md5()
    md5_hash.update(passwd.encode("utf-8"))
    md5_code = md5_hash.hexdigest()
    return md5_code


# 验证账号是否被锁定
def Account_locked(username):
    with open(lock_name_file,'r') as L:
        for Line in L.readlines():
            Lines = Line.split()
            if username == Lines[0]:
                print("%s 账号已经被锁定，请联系管理员解锁账号" % username)
                sys.exit()
            else:
                continue


# 验证账号密码
def Account_validation(username, Md5_passwd):
    with open(account_file,'r') as f:
        for line in f.readlines():
            lines = line.split()
            if len(lines) != 0:
              print('账号或密码有问题，请联系管理员处理')
              sys.exit()
            elif username == lines[0]:
                if Md5_passwd == lines[1]:
                    print("欢迎  %s 登录" % username)
                    sys.exit()
                else:
                    validation = 0
                    return validation
            else:
                continue


# 验证账号是否存在
def Account_exists(username):
    with open(account_file,'r') as f:
        for line in f.readlines():
            lines = line.split()
            if lines == []:
                exists = 0
                return exists
            if username == lines[0]:
                exists = 1
                return exists


# 配置并保存密码
def Save_password():
    passwd = input("请设置密码（必须包含数字、大小字母，且长度不小于5位，特殊符号可选）：").strip()
    if len(passwd) >= 5 and re.search('[0-9]', passwd) and re.search('[a-z]', passwd) and re.search('[A-Z]', passwd):
        passwd_confirmation = input("确认密码：").strip()
        if passwd == passwd_confirmation:
            V_code = Verification_code()
            print('本次验证码为：%s ' % V_code)
            V_code_user = input('请输入验证码：').strip()
            if len(V_code_user) != 0 and V_code_user == V_code:
                return Md5_code(passwd)
            else:
                print('验证码不正确，请重新配置密码')
                Save_password()
        else:
            print('两次输入的密码不相同，请重新配置密码')
            Save_password()

    else:
        print('您设置的密码不符合要求，请重新设置')
        Save_password()


# 登陆
def Sign_in():
    global login_times
    username = input("请输入用户名：").strip()
    passwd = input("请输入密码：").strip()

    V_code = Verification_code()
    print('本次验证码为：%s ' % V_code)
    V_code_user = input('请输入验证码：').strip()
    if len(V_code_user) != 0 and V_code_user == V_code:
        Account_locked(username)
        Md5_passwd = Md5_code(passwd)
        Account_validation(username, Md5_passwd)
        validation = Account_validation(username, Md5_passwd)
        if validation == 0:
            login_times += 1
            if login_times == 3:
                with open(lock_name_file, 'a') as user_lock:
                    user_lock.write(username + '\n')
                print("用户名、密码错误三次，%s 账号已被锁定，请联系管理员解锁账号" % username)
                sys.exit()
            print('账号或密码错误，请重新登陆')
            Sign_in()
        if validation == None:
            print('账号或密码错误，请重新登陆')
            Sign_in()
    else:
        print('验证码错误')
        Sign_in()


# 注册
def Sign_up():
    username = input("请输入用户名：").strip()
    if len(username) == 0:
        print('请输入正确的用户名')
        Sign_up()
    user_exists = Account_exists(username)
    if user_exists == 1:
        print('%s用户已经存在，请重新配置用户名' % username)
        Sign_up()
    else:
        Md5_user_passwd = Save_password()
        with open(account_file, 'a') as user_add:
            user_add.write('%s\t%s\n' % (username, Md5_user_passwd))
        print("账号 %s 注册成功" % username)
        print("欢迎  %s 登录" % username)
        sys.exit()


# 开始使用系统
def Start():
    print('欢迎使用')
    User = ['新用户注册', '老用户登录']
    for i in enumerate(User):
        print(i[0], i[1])
    start_status = input('请选您要进行的操作(0 or 1)：').strip()
    if start_status.isdigit() and int(start_status) <= 1:
        if int(start_status) == 0:
            Sign_up()
        else:
            Sign_in()
    else:
        print('您的输入有误')
        sys.exit()


# 主程序
if __name__ == '__main__':
    Start()

