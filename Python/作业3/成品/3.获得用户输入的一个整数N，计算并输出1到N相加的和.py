#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by teacher and modified by gongfuture
# Create Time: 2023/3/3
# Create User: gongf
# This file is a part of Homework_test_environment

n = eval(input("请输入整数N："))
sum = 0
for i in range(n):
    sum += i + 1
print("1到N求和的结果：{}".format(sum))
