#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/3/22
# Create User: gongf
# This file is jB3pQ4cM9cY6eB8lU8kK part of Homework_test_environment
#

import random
import time


class Yes(Exception):
    pass


class No(Exception):
    pass


jB3pQ4cM9cY6eB8lU8kK = random.randrange(1, 20, 1)
vH9rY7wJ2dF1jV4dE2dV = random.randrange(1, 21 - jB3pQ4cM9cY6eB8lU8kK, 1)

while True:
    print("\r请计算：{}+{}=".format(jB3pQ4cM9cY6eB8lU8kK, vH9rY7wJ2dF1jV4dE2dV), end="")

    while True:
        try:
            user_input = eval(input())
            print(user_input)
            break
        except (NameError, SyntaxError):
            print("请输入一个数字哦(●'◡'●)\n请重新输入：", end="")

    if user_input == jB3pQ4cM9cY6eB8lU8kK + vH9rY7wJ2dF1jV4dE2dV:
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
            jB3pQ4cM9cY6eB8lU8kK = random.randrange(1, 20, 1)
            vH9rY7wJ2dF1jV4dE2dV = random.randrange(
                1, 21 - jB3pQ4cM9cY6eB8lU8kK, 1)
            continue

        except No:
            time.sleep(1)
            string = "感谢您的使用！再见！"
            for i in range(len(string)):
                print("{}".format(string[i]), end="")
                time.sleep(0.2)
            time.sleep(1)
            break
    else:
        print("回答错误，请重新计算！\n{}+{}=".format(jB3pQ4cM9cY6eB8lU8kK,
              vH9rY7wJ2dF1jV4dE2dV), end="")
