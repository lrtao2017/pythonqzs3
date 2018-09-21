#!/usr/bin/env python 
__author__ = "lrtao2010" 

import xlrd
import csv

def xlsx_to_csv():
    workbook = xlrd.open_workbook('1.xlsx')
    table = workbook.sheet_by_index(0)
    with open('1.csv', 'w', encoding='utf-8',newline='') as f: #newline=''不加会多空行
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