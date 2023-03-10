#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/10
# Create User: gongf
# This file is a part of Homework_test_environment

print("请输入字符串", end="：")
s = input()
s = s.replace('，', '')
s = s.replace('。', '')
# todo:试试用sub函数实现
print("中文字符数为{}".format(len(s)))
