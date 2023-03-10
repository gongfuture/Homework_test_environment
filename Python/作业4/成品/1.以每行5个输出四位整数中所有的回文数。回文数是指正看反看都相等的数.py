#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/10
# Create User: gongf
# This file is a part of Homework_test_environment

count = 0
five = 0
for i in range(1000, 10000):
    a = str(i)
    if a[0] == a[-1] and a[1] == a[-2]:
        count += 1
        print(i, end=' ')
        five += 1
        if five == 5:
            five = 0
            print("", end='\n')
print(count)
