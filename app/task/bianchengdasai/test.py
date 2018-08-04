#!/usr/bin/env python
__author__ = "lrtao2010"

# name_info = {
#     'alex': {
#         'passwd':'alex123',
#         'locked':'0',
#         'role':'管理员',
#         'card':'300',
#         'borrow_book':[]
#         },
#     'pizza': {
#         'passwd':'pizza123',
#         'locked':'0',
#         'role':'教师',
#         'card':'300',
#         'borrow_book':[]
#         },
#     'john':{
#         'passwd':'john123',
#         'locked':'0',
#         'role':'学生',
#         'card':'300',
#         'borrow_book':[]
#         },
# }
# name_passwd_list = []
#
# for name in name_passwd.keys():
#     name_passwd_list_item = []
#     name_passwd_list_item.append(name)
#     for k,v in name_passwd[name].items():
#         if k == 'borrow_book':
#             name_passwd_list_item.extend(v)
#         else:
#             name_passwd_list_item.append(v)
#     name_passwd_list.append(name_passwd_list_item)
# name_passwd_list_str = '\n'.join(','.join(item) for item in name_passwd_list)
# user_file = 'user.txt'
# with open(user_file, 'w', encoding='utf-8') as userf:
#     userf.write(name_passwd_list_str)



# name_info = {}
# user_file = 'user.txt'
# with open(user_file, 'r+', encoding='utf-8') as user_r_f:
#     for lines in user_r_f.readlines():
#         line = lines.strip().split(',')
#         borrow_book_o = line[5:] if len(line) > 5 else []
#         name_info[line[0]]={
#             'passwd':line[1],
#             'locked':line[2],
#             'role':line[3],
#             'card':line[4],
#             'borrow_book':borrow_book_o
#         }
user_file = 'test.txt'
name_info_list_str = 'A'
with open(user_file, 'w', encoding='utf-8') as userf:
    userf.write(name_info_list_str)