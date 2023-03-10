#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/10 
# Create User: gongf
# This file is a part of Homework_test_environment

print("请选择加密还是解密，1加密，2解密", end='：')
choose = input()
if choose == "1":
	print("请输入原文", end='：')
	input_in = input()
	print("密文为", end='：')
	for i in input_in:
		if "a" <= i <= "z":
			print(chr(ord("a") + (ord(i) - ord("a") + 5) % 26), end="")
		elif "A" <= i <= "Z":
			print(chr(ord("A") + (ord(i) - ord("A") + 5) % 26), end="")
		else:
			print(i, end="")
if choose == "2":
	print("请输入密文", end='：')
	input_in = input()
	print("原文为", end='：')
	for i in input_in:
		if "a" <= i <= "z":
			print(chr(ord("a") + (ord(i) - ord("a") - 5) % 26), end="")
		elif "A" <= i <= "Z":
			print(chr(ord("A") + (ord(i) - ord("A") - 5) % 26), end="")
		else:
			print(i, end="")
