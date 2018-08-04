#!/usr/bin/env python
__author__ = "lrtao2010"

name_passwd = {
    'alex': ['alex123','管理员'],
    'pizza': ['pizza123','教师'],
    'john': ['john123','学生']
}
# locked_account_file = "lock.txt"
# book_file = "book.txt"
# error_count = 0
# allow_login = True
# account_is_no_locked = True
# login_successful = False
#
# borrow_book = [] #借书列表
# #登录系统
# while allow_login :
#     user_name = input("请输入用户名：" ).strip().lower()
#     user_password = input("请输入密码：")
#
#     if error_count == 0:
#         # 检查账号是否被锁定
#         with open(locked_account_file, 'r') as L:
#             for Line in L.readlines():
#                 Lines = Line.split()
#                 if Lines != [] and user_name == Lines[0]:
#                     #!=[]防止locked_account_file中有空行报错
#                     print("%s 账号已经被锁定，请联系管理员解锁账号" % user_name)
#                     allow_login = False
#                     account_is_no_locked = False
#
#
#         user_name_old = user_name
#
#     # 从第二次输入开始判断用户名是否和上次一致
#     if error_count > 0 and user_name_old != user_name:
#         print('请输入第一次输入的用户名')
#         continue
#
#     # 验证账号密码
#     if account_is_no_locked :
#         if user_name in name_passwd.keys():
#             if user_password == name_passwd[user_name][0]:
#                 print('\033[1;36m%s %s 您好，欢迎光临!\033[0m' % (name_passwd[user_name][1],user_name))
#                 allow_login = False
#                 login_successful = True
#             else:
#                 print("用户名或密码错误")
#                 error_count += 1
#                 left_count = 3 - error_count
#                 print('您还有 %s 次重试机会'  % left_count)
#                 # 存在的账号密码错误三次被锁定
#                 if error_count == 3:
#                     with open(locked_account_file, 'a') as user_lock:
#                         user_lock.write(user_name.strip() + '\n')
#                     print("用户名、密码错误三次，%s 账号已被锁定，请联系管理员解锁账号" % user_name)
#                     allow_login = False
#         else:
#             print("用户名或密码有问题，请联系管理员处理")
#             allow_login = False
#
# #登录成功后，可以进行下面的操作
#
# if login_successful:
#     if name_passwd[user_name][1] == "管理员":
#         pass
#     else:
#         #生成用户已经借阅的图书列表
#         user_borrow_book_file = "%s_borrow_book.txt" % user_name
#         with open(user_borrow_book_file, 'r+', encoding='utf-8') as uf:
#             for book_name in uf.readlines():
#                 borrow_book = book_name.split(',')
#         #生成图书馆图书列表
#         with open(book_file, 'r', encoding='utf-8') as bf:
#             for book_name in bf.readlines():
#                 book_name_list = book_name.split(',')
#
#         exit_app = False
#         while not exit_app:
#             print('B(借书)', 'R(还书)','E(退出系统)')
#             operating=input("请选择要进行的操作(B/R/E(B)):").strip()
#             #借书
#             if operating == 'B' or operating == 'b' or operating == '':
#                 borrow_again = True
#                 while borrow_again:
#                     print('现在可以借阅的图书有：')
#                     for id,book in enumerate(book_name_list):
#                         print(id,book)
#                     book_name_id_str = input('请选择要要借阅的图书编号：').strip()
#                     if book_name_id_str != 0:
#                         book_name_id = int(book_name_id_str)
#                         if book_name_id <= len(book_name_list):
#                             #将借阅的图书添加的用户借阅列表，并从图书馆图书列表中删除
#                             borrow_book.append(book_name_list.pop(book_name_id))
#                             print('您现在借阅的图书有：')
#                             for book in borrow_book:
#                                 print(book)
#                             borrow_again_input = input('是否继续借阅图书(y/n (n))').strip()
#                             if borrow_again_input != 'y':
#                                 borrow_again = False
#                     else:
#                         print('输入有误，请重新选择')
#
#
#
#             elif operating == 'R' or operating == 'r':
#                 pass
#             elif operating == 'E' or operating == 'e':
#                 #报存图书馆图书列表
#                 book_name_str = ",".join(book_name_list)
#                 with open(book_file, 'w',encoding='utf-8') as lbook_name:
#                     lbook_name.write(book_name_str.strip())
#                 # 报存用户借阅图书列表
#                 with open(user_borrow_book_file, 'w', encoding='utf-8') as ubook_name:
#                     ubook_name.write(borrow_book.strip())
#
#                 print('谢谢使用，再见！')
#                 exit_app = True
#             else:
#                 print('输入有误，请重新选择')
#                 continue