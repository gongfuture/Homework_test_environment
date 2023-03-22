#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/22 
# Create User: gongf
# This file is a part of Homework_test_environment
#

import random

a = random.randrange(1, 19, 1)
b = random.randrange(1, 19-a, 1)
while 1:
	print("\r请计算：{}+{}=".format(a, b), end="")
	user_input = input()
	if user_input == a + b:
		print("恭喜您回答正确，请问是否继续计算？(y/n)", end="")
		yn = input()
		if yn == "y":

	else:
		print("回答错误，请重新计算！\n{}+{}=".format(a, b), end="")
