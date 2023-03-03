#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/2/19
# Create User: gongf
# This file is a part of Homework_test_environment

from turtle import *

setup(650, 350, 200, 200)

penup()
fd(200)
pendown()
pensize(25)
pencolor("purple")
fd(40 * 2 / 3)
circle(-16, 180)
fd(40)
circle(-40, 80 / 2)

for i in range(4):
    circle(40, 80)
    circle(-40, 80)
done()
