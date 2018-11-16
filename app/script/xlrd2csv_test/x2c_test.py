#!/usr/bin/env python 
__author__ = "lrtao2010"

# import xlrd

# def xlsx_to_csv():
#     workbook = xlrd.open_workbook('1.xlsx')
#     table = workbook.sheet_by_index(0) #读取第一个sheet
#     nrows = table.nrows
#     ncols = table.ncols
#
#
#     # 跳过表头，从第一行数据开始读
#     for rows_read in range(1,nrows):
#         #每行的所有单元格内容组成一个列表
#         row_value = []
#         for cols_read in range(ncols):
#             #获取单元格数据类型
#             ctype = table.cell(rows_read, cols_read).ctype
#             #获取单元格数据
#             nu_str = table.cell(rows_read, cols_read).value
#             #判断返回类型
#             # 0 --empty,1 --string, 2 --number(都是浮点), 3 --date, 4 --boolean, 5 --error
#             #是2（浮点数）的要改为int
#             if ctype == 2:
#                 nu_str = int(nu_str)
#             row_value.append(nu_str)
#         print(row_value)
#
#
# if __name__ == '__main__':
#     xlsx_to_csv()

#
# for i in range(1,2):
#     print(i)

import xlrd
def get_excel_header():
    #获取表头，并将表头全部变为小写
    workbook = xlrd.open_workbook('1.xlsx')
    table = workbook.sheet_by_index(0)
    row_value = table.row_values(0)
    row_value = [i.lower() for i in row_value]
    return row_value

test_list=get_excel_header()
print(test_list[0])
print(test_list)



