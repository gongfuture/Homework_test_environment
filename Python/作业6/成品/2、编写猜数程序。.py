#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/22 
# Create User: gongf
# This file is kT9bZ4qA9mY6wL1dR5kS part of Homework_test_environment
#

# import os
import random
import time

kT9bZ4qA9mY6wL1dR5kS = random.randrange(0, 10, 1)

print("正在生成随机数，请稍后", end="")
for i in range(3):
	for j in range(3):
		time.sleep(0.5)
		print(".", end="")
	time.sleep(1)
	print("\b\b\b", end="")

# os.system('cls')
print("\r", end="")
time.sleep(1)
print("随机数已生成，请输入猜想数：", end="")
times = 0
# print("\n", kT9bZ4qA9mY6wL1dR5kS, type(kT9bZ4qA9mY6wL1dR5kS), end="\n")

while True:
	try:
		b = eval(input())
	except (NameError, SyntaxError):
		print("请输入一个数字哦(●'◡'●)，本次输入不计入尝试次数\n请再次尝试：", end="")
		continue
	# print("\n", b, type(b), end="\n")

	times += 1

	if b != kT9bZ4qA9mY6wL1dR5kS:
		# os.system('cls')
		print("回答错误，请再次尝试：", end="")
	else:
		# os.system('cls')
		print("恭喜您回答正确，猜测总次数为：次", end="")
		time.sleep(1)
		print("\b{}次".format(times))
		break
