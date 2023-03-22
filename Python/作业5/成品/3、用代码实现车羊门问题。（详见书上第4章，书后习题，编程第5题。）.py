#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/17
# Create User: gongf
# This file is a part of Homework_test_environment
#
from random import *
times = 100000
change_times = 0
no_change_times = 0
for i in range(times):
    real = randint(0, 2)
    guess = randint(0, 2)
    if (real == guess):
        no_change_times += 1
    else:
        change_times += 1
print(
    "不改选择选中概率:{}\n更改选择选中概率:{}".format(
        no_change_times /
        times,
        change_times /
        times))
