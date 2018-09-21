#!/usr/bin/env python 
__author__ = "lrtao2010" 

import xlrd
import csv
import os

def xlsx_to_csv():
    file_list = os.listdir(os.getcwd())
    for file_name in file_list:
        if file_name.endswith('xlsx') or file_name.endswith('xls'):
            workbook = xlrd.open_workbook(file_name)
            table = workbook.sheet_by_index(0)
            with open('1.csv', 'a', encoding='utf-8',newline='') as f: #newline=''不加会多空行
                write = csv.writer(f)
                for row_num in range(table.nrows):
                    row_value = table.row_values(row_num)
                    write.writerow(row_value)

if __name__ == '__main__':
    xlsx_to_csv()

# def xlsx_to_csv():
#     workbook = xlrd.open_workbook('1.xlsx')
#     table = workbook.sheet_by_index(0)
#
#
#     for row_num in range(table.nrows):
#         row_value = table.row_values(row_num)
#         print(row_value)
#
#
# if __name__ == '__main__':
#     xlsx_to_csv()