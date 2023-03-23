#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/22 
# Create User: gongf
# This file is a part of Homework_test_environment
#

import random


class Yes(Exception):
	pass


class No(Exception):
	pass


a = random.randrange(1, 20, 1)
b = random.randrange(1, 21 - a, 1)

while True:
	print("\r请计算：{}+{}=".format(a, b), end="")

	try:
		user_input = eval(input())
		print(user_input)
	except (NameError, SyntaxError):
		print("请输入一个数字哦(●'◡'●)", end="")
		continue


	if user_input == a + b:
		print("\r恭喜您回答正确，请问是否继续计算？(y/n)", end="")

		try:
			while 1:
				yn = input()
				if yn == "y":
					raise Yes
				elif yn == "n":
					raise No
				else:
					print("\r请输入y或n！", end="")
					continue

		except Yes:
			a = random.randrange(1, 20, 1)
			b = random.randrange(1, 21 - a, 1)
			continue

		except No:
			break
	else:
		print("回答错误，请重新计算！\n{}+{}=".format(a, b), end="")
