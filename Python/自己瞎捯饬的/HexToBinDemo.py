#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/10/27
# Create User: gongf
# This file is a part of Homework_test_environment
#
import os


def hex_to_bin(hex_string):
    decimal_number = int(hex_string.replace(' ', ''), 16)
    binary_number = bin(decimal_number)
    return binary_number[2:]


print("请输入输出文件储存地址：", end=" ")
path = input()
print("请输入输出文件后缀：", end=" ")
file_end = input()
print("请粘贴需转化的HEX：", end=' ')
hex_string = input()
binary_string = hex_to_bin(hex_string)
file = open(path + 'output' + file_end, 'w')
file.write(binary_string)
file.close()
