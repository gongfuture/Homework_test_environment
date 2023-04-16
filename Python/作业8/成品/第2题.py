#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/4/16 
# Create User: gongf
# This file is a part of Homework_test_environment
#

movies = {
'妖猫传':['黄轩','染谷将太'],
'无问西东':['章子怡','王力宏','祖峰'],
'超时空同居':['雷佳音','佟丽娅'],
}

actor = input('你想查询哪个演员？')
for movie, actors in movies.items():
    if actor in actors:
        print("{}出演了电影{}".format(actor, movie))
