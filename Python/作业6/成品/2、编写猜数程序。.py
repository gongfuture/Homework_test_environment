#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/22 
# Create User: gongf
# This file is a part of Homework_test_environment
#

import random
import time

a = random.randrange(0, 10, 1)
print("正在生成随机数，请稍后", end="")
# for i in range(3):
# 	for j in range(3):
# 		time.sleep(0.5)
# 		print(".", end="")
# 	time.sleep(1)
# 	print("\b\b\b", end="")
print("\r随机数已生成，请输入猜想数：", end="")
print(a)
b = input()
times = 0
while b != a:
	times += 1
	print("\r回答错误，请再次尝试：", end="")
	b = input()
else:
	times += 1
	print("\r恭喜您回答正确，猜测总次数为：", end="")
	time.sleep(1)
	print(times)
