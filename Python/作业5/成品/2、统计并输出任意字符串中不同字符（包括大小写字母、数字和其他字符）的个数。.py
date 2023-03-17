#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/17 
# Create User: gongf
# This file is a part of Homework_test_environment
#

print("请输入字符串", end="：")
keyboard_input = input()
count_language = count_space = count_num = count_other = 0

for s in keyboard_input:
	if s.isalpha():
		count_language += 1
	elif s.isdigit():
		count_num += 1
	elif s.isspace():
		count_space += 1
	else:
		count_other += 1

print("文字数量：{}\n数字数量：{}\n空格数量：{}\n其他字符数量：{}".format(count_language, count_num, count_space, count_other))