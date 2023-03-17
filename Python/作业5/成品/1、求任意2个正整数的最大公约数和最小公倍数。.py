#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/17 
# Create User: gongf
# This file is a part of Homework_test_environment
#

import re

print("请依次输入两个整数", end="：")  # 屏幕输出
keyboard_input = input("")  # 用户输入
keyboard_input = list(filter(None,re.split("[, ，、；;]", keyboard_input)))  # 分割数字
keyboard_input = [int(keyboard_input[i]) for i in range(len(keyboard_input))]  # 将字符串整形化

# print(keyboard_input)
# print(len(keyboard_input))

if len(keyboard_input) != 2:  # 检测输入数据格式
	print("你输入的数字个数或格式不对，程序即将退出。")
	exit(2)

else:
	a = keyboard_input[0]  # 赋值
	b = keyboard_input[1]
	x = a * b
	# print(a, b, x)

	while b != 0:  # 辗转相除
		d = a % b
		a = b
		b = d
		# print(a, b, d)

	zdgys = a
	zxgbs = x / zdgys
	print("最大公约数是：{}\n最小公倍数是：{:.0f}".format(zdgys, zxgbs))
	exit(1)
