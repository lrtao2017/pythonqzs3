#!/usr/bin/env python
__author__ = "lrtao2010"


user_file = 'user.txt'  #存放用户信息的文件
book_file = "book.txt"  #存放图书馆图书信息的文件
error_count = 0
login_successful = False
name_info = {} #用户信息
borrow_book = [] #借书列表

#生成用户信息
with open(user_file, 'r+', encoding='utf-8') as user_r_f:
    for lines in user_r_f.readlines():
        line = lines.strip().split(',')
        borrow_book_o = line[5:] if len(line) > 5 else []
        name_info[line[0]]={
            'passwd':line[1],
            'locked':line[2],
            'role':line[3],
            'card':line[4],
            'borrow_book':borrow_book_o
        }

#登录系统
while error_count < 3 :
    user_name = input("请输入用户名：" ).strip().lower()
    user_password = input("请输入密码：")

    if error_count == 0:
        # 检查账号是否被锁定
        if user_name in name_info.keys():
            if name_info[user_name]['locked'] == '1':
                print("\033[1;31m%s 账号已经被锁定，请联系管理员解锁账号\033[0m" % user_name)
                break
        else:
            print("\033[1;31m用户名或密码有问题，请联系管理员处理\033[0m")
            break
        user_name_old = user_name

    # 从第二次输入开始判断用户名是否和上次一致
    if error_count > 0 and user_name_old != user_name:
        print('\033[1;31m请输入第一次输入的用户名\033[0m')
        continue

    # 验证账号密码

    if user_password == name_info[user_name]['passwd']:
        print('\033[1;36m%s %s 您好，欢迎光临!\033[0m' % (name_info[user_name]['role'],user_name))
        login_successful = True
        break

    else:
        print("\033[1;31m用户名或密码错误\033[0m")
        error_count += 1
        left_count = 3 - error_count
        print('\033[1;36m您还有 %s 次重试机会\033[0m'  % left_count)
        # 存在的账号密码错误三次被锁定
        if error_count == 3:
            name_info[user_name]['locked'] = '1'
            print("\033[1;31m用户名、密码错误三次，%s 账号已被锁定，请联系管理员解锁账号\033[0m" % user_name)

            #将锁定信息保留到文件
            name_info_list = []
            for name in name_info.keys():
                name_info_list_item = []
                name_info_list_item.append(name)
                for k,v in name_info[name].items():
                    if k == 'borrow_book':
                        name_info_list_item.extend(v)
                    else:
                        name_info_list_item.append(v)
                name_info_list.append(name_info_list_item)
            name_info_list_str = '\n'.join(','.join(item) for item in name_info_list)
            user_file = 'user.txt'
            with open(user_file, 'w', encoding='utf-8') as userf:
                userf.write(name_info_list_str)
            break


#登录成功后，可以进行下面的操作

if login_successful:
    # 生成图书馆图书列表
    book_name_list = []
    with open(book_file, 'r', encoding='utf-8') as bf:
        for book_name in bf.readlines():
            book_name_list = book_name.split(',')

    #管理员可以进行的操作
    if name_info[user_name]['role'] == "管理员":
        admin_exit_app = False
        while not admin_exit_app:
            print('\n')
            print('\033[1;36mU(修改用户信息)', 'B(修改图书信息)', 'E(退出系统)\033[0m')
            admin_operating = input("\033[1;36m请选择要进行的操作(U/B/E (B)):\033[0m").strip()
            if admin_operating == 'B' or admin_operating == 'b' or admin_operating == '':
                print('\033[1;36m图书馆总共有图书：\033[0m')
                for book in name_info[user_name]['borrow_book']:
                    print(book)
                print('\033[1;36m现在可以借阅的图书有：\033[0m')
                for book in book_name_list:
                    print(book)
                modify = True
                print('\033[1;31m输入存在的图书名将会删除该图书，输入不存在的图书名将会新增该图书\033[0m')
                while modify:
                    book_name1 = input('\033[1;36m请输入要修改的图书名：\033[0m')
                    book_name2 = input('\033[1;36m请再次输入要修改的图书名：\033[0m')
                    if book_name1 != book_name2:
                        print('\033[1;31m两次输入的图书名不一样，请核实后在操作\033[0m')
                    else:
                        #输入的图书名存在就删除，不存在就添加
                        if (book_name1 in name_info[user_name]['borrow_book']) and (book_name1 not in book_name_list):
                            print('\033[1;31m图书：%s 已经被借走，暂时不能修改该书的信息\033[0m' % book_name1)
                            break
                        elif book_name1 in name_info[user_name]['borrow_book']:
                            name_info[user_name]['borrow_book'].remove(book_name1)
                            book_name_list.remove(book_name1)
                            print('\033[1;36m删除图书：%s\033[0m' % book_name1)
                        elif book_name1 not in name_info[user_name]['borrow_book']:
                            name_info[user_name]['borrow_book'].append(book_name1)
                            book_name_list.append(book_name1)
                            print('\033[1;36m新增图书：%s\033[0m' % book_name1)
                        modify_again = input("\033[1;36m是否继续修改y/n (n) :\033[0m")
                        if modify_again != 'y':
                            modify = False

            elif admin_operating == 'U' or admin_operating == 'u':
                print('\033[1;36m现有用户信息如下：\033[0m')
                for k in name_info.keys():
                    v = name_info[k]['role']
                    print(('%s  %s') % (v,k))
                print('\033[1;31m输入存在的用户名将会删除该用户，输入不存在的用户名将会新增该用户\033[0m')
                print("\033[1;31m管理员账号‘alex' 不能被修改\033[0m")
                user_modify = True
                while user_modify:
                    user_name1 = input('\033[1;36m请输入要修改的用户名：\033[0m')
                    user_name2 = input('\033[1;36m请再次输入要修改的用户名：\033[0m')
                    if user_name1 != user_name2:
                        print('\033[1;31m两次输入的用户名不一样，请核实后在操作\033[0m')
                    else:
                        if user_name1 == 'alex':
                            print('\033[1;31m管理员账号不能修改\033[0m')
                        elif user_name1 in name_info.keys():
                            name_info.pop(user_name1)
                            print('\033[1;36m删除用户 %s\033[0m' % user_name1)
                        else:
                            user_role = input("\033[1;36m请输入该用户的角色：\033[0m")
                            name_info[user_name1]={
                                'passwd':'%s123' % user_name1,
                                'locked':'0',
                                'role':'%s' % user_role,
                                'card':'300'
                            }
                            print('\033[1;36m新增用户%s \033[0m' % user_name1)
                        user_modify_again = input("\033[1;36m是否继续修改y/n (n) :\033[0m")
                        if user_modify_again != 'y':
                            user_modify = False

            elif admin_operating == 'E' or admin_operating == 'e':
                # 保存图书馆图书列表到文件
                book_name_str = ",".join(book_name_list)
                with open(book_file, 'w', encoding='utf-8') as lbook_name:
                    lbook_name.write(book_name_str.strip())

                # 保存用户信息到文件
                name_info_list = []
                for name in name_info.keys():
                    name_info_list_item = []
                    name_info_list_item.append(name)
                    for k, v in name_info[name].items():
                        if k == 'borrow_book':
                            name_info_list_item.extend(v)
                        else:
                            name_info_list_item.append(v)
                    name_info_list.append(name_info_list_item)
                name_info_list_str = '\n'.join(','.join(item) for item in name_info_list)
                user_file = 'user.txt'
                with open(user_file, 'w', encoding='utf-8') as userf:
                    userf.write(name_info_list_str)

                print('\033[1;36m谢谢使用，再见！\033[0m')
                admin_exit_app = True

            else:
                print('\033[1;31m输入有误，请重新选择\033[0m')
                continue



    #普通用户可以进行的操作
    else:
        #生用户已经借阅的图书列表
        borrow_book = name_info[user_name]['borrow_book']
        if len(borrow_book) != 0:
            print('\033[1;36m您现在借阅的图书有：\033[0m')
            for book in borrow_book:
                print(book)

        user_card = int(name_info[user_name]['card'])  # 获取卡上余额
        exit_app = False
        while not exit_app:
            print('\033[1;36mB(借书)', 'R(还书)','E(退出系统)\033[0m')
            operating=input("\033[1;36m请选择要进行的操作(B/R/E (B)):\033[0m").strip()
            #借书
            if operating == 'B' or operating == 'b' or operating == '':
                borrow_again = True
                while borrow_again:
                    if user_card == 0:
                        print("\033[1;31m你卡上的余额不足，请先还书，再来借书\033[0m")
                        break
                    if len(book_name_list) == 0:
                        print("\033[1;31m现在图书馆的书都借出去了，请改天再来\033[0m")
                        break
                    print('\033[1;36m现在可以借阅的图书有：\033[0m')
                    for id,book in enumerate(book_name_list):
                        print(id,book)
                    book_name_id = input('\033[1;36m请选择要要借阅的图书编号：\033[0m').strip()
                    if book_name_id.isdigit() and int(book_name_id) <= len(book_name_list):
                        #将借阅的图书添加的用户借阅列表，并从图书馆图书列表中删除
                        borrow_book.append(book_name_list.pop(int(book_name_id)))
                        user_card -= 100
                        print('\033[1;36m您现在借阅的图书有：\033[0m')
                        for id,book in enumerate(borrow_book):
                            print(id,book)
                        borrow_again_input = input('\033[1;36m是否继续借阅图书(y/n (n))\033[0m').strip()
                        if borrow_again_input != 'y':
                            borrow_again = False
                    else:
                        print('\033[1;31m输入有误，请重新选择\033[0m')
            #还书
            elif operating == 'R' or operating == 'r':
                r_again_input = True
                while r_again_input:
                    if len(borrow_book) == 0:
                        print("\033[1;36m您现在没有借阅任何图书\033[0m")
                        break
                    print('\033[1;36m您现在借阅的图书有：\033[0m')
                    for id, book in enumerate(borrow_book):
                        print(id, book)
                    r_book_id = input('\033[1;36m请输入要还书的编号：\033[0m').strip()
                    if r_book_id.isdigit() and int(r_book_id) <= len(borrow_book):
                        # 将要还的图书添加到图书馆图书列表，并从用户借阅列表中删除
                        book_name_list.append(borrow_book.pop(int(r_book_id)))
                        user_card += 100
                        if len(borrow_book) != 0:
                            print('\033[1;36m您现在借阅的图书有：\033[0m')
                            for id, book in enumerate(borrow_book):
                                print(id, book)
                            r_again_input = input('\033[1;36m是否继续还书书(y/n (n))\033[0m').strip()
                            if r_again_input != 'y':
                                r_again_input = False
                        else:
                            print('\033[1;36m您现在没有借阅任何图书\033[0m')
                            r_again_input = False
                    else:
                        print('\033[1;31m输入有误，请重新选择\033[0m')
            #退出系统
            elif operating == 'E' or operating == 'e':
                #保存图书馆图书列表到文件
                book_name_str = ",".join(book_name_list)
                with open(book_file, 'w',encoding='utf-8') as lbook_name:
                    lbook_name.write(book_name_str.strip())

                # 保存用户信息到文件
                name_info[user_name]['borrow_book'] = borrow_book
                name_info[user_name]['card'] = str(user_card)
                name_info_list = []
                for name in name_info.keys():
                    name_info_list_item = []
                    name_info_list_item.append(name)
                    for k, v in name_info[name].items():
                        if k == 'borrow_book':
                            name_info_list_item.extend(v)
                        else:
                            name_info_list_item.append(v)
                    name_info_list.append(name_info_list_item)
                name_info_list_str = '\n'.join(','.join(item) for item in name_info_list)
                user_file = 'user.txt'
                with open(user_file, 'w', encoding='utf-8') as userf:
                    userf.write(name_info_list_str)

                #打印当前借阅图书情况
                if len(borrow_book) != 0:
                    print('\033[1;36m您现在借阅的图书有：\033[0m')
                    for book in borrow_book:
                        print(book)
                else:
                    print('\033[1;36m您现在没有借阅任何图书\033[0m')
                print('\033[1;36m谢谢使用，再见！\033[0m')
                exit_app = True
            else:
                print('\033[1;31m输入有误，请重新选择\033[0m')
                continue
