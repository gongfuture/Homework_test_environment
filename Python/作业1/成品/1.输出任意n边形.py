#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/2/19
# Create User: gongf
# This file is a part of Homework_test_environment

from turtle import *

n = eval(input("请输入需要的边数："))
# speed(1)    # 更改速度测试用
setup(650, 400, 200, 200)
pensize(3)
penup()
goto(50, 50)
pendown()
begin_fill()
color('black')
circle(40, steps=n)
end_fill()

# input()  # 需要暂停时启用
