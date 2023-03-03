#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/3
# Create User: gongf
# This file is a part of Homework_test_environment

print("请依次输入x0,y0,x1,y1，并使用空格隔开四个数", end="：")
keyboard_input = input("")
x0, y0, x1, y1 = keyboard_input.split(" ")
x0, y0, x1, y1 = float(x0), float(y0), float(x1), float(y1)
distance = pow(pow(x1 - x0, 2) + pow(y1 - y0, 2), 0.5)
print("{:.2f}".format(distance))
