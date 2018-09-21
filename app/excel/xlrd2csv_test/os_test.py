#!/usr/bin/env python 
__author__ = "lrtao2010" 

import os

file_list=os.listdir(os.getcwd())
for file_name in file_list:
    if file_name.endswith('csv'):
        print(file_name)