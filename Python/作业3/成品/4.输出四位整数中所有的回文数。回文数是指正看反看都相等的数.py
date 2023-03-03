#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/3
# Create User: gongf
# This file is a part of Homework_test_environment

# print("请输入需要输出的回文数范围,以空格分隔", end="：")
# in_put = input()
# min_in, max_in = in_put.split('')
# min_in, max_in = float(min_in), float(max_in)
# count = 0
# for i in range(min_in, max_in):
# 	a = str(i)
#     for n in range(len(min_in),len(max_in))
# 	if a[0] == a[-1] and a[1] == a[-2]:
# 		count += 1
# 		print(i)
# print(count)


# Code copied from https://www.cnblogs.com/dabai123/p/10960609.html
count = 0
for i in range(1000, 10000):
    a = str(i)
    if a[0] == a[-1] and a[1] == a[-2]:
        count +=1
        print(i)
# print(count)
