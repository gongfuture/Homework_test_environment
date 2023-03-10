#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/10
# Create User: gongf
# This file is a part of Homework_test_environment

print("请输入需要输出第几个Fibnacci数", end='：')
n = int(input())
a, b = 0, 1
for i in range(n - 1, n):
    print(a, end=" ")
    a, b = b, a + b
