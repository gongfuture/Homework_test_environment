#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/2/20
# Create User: gongf
# This file is a part of Homework_test_environment

import turtle

turtle.setup(1000, 400)
turtle.penup()
turtle.pensize(2)
turtle.color("black")
turtle.goto(-400, -50)
turtle.seth(45)
# turtle.speed(1)    #测试使用，减缓动画速度
i = 1
while i < 6:
	turtle.pendown()
	turtle.circle(80 / 2 ** 0.5, steps=4)
	turtle.penup()
	turtle.goto(-400 + 160 * i, -50)
	i = i + 1
