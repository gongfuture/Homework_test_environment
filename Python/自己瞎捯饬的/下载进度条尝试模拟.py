#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/10/16 
# Create User: gongf
# This file is a part of Homework_test_environment
#
import time
import random

try_times = 5


def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


print("请输入需要模拟的下载总量：", end='')
for i in range(try_times):
    total = input()
    if is_float(total):
        # print({total})
        break
    else:
        print("Invalid")
    if i == try_times - 1:
        print("Invalid2")
