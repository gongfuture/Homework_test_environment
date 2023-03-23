#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/22
# Create User: gongf
# This file is a part of Homework_test_environment
#
import re

print("请输入字符串", end="：")
while True:
    keyboard_input = input()
    if bool(re.search(r'\d', keyboard_input)):
        print("输入有数字，请重新输入：", end="")
        continue
    else:
        print("{}".format(len(keyboard_input)))
        break
