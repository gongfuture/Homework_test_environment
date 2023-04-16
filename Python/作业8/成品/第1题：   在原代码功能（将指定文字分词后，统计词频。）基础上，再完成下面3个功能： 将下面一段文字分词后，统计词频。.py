#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/4/16 
# Create User: gongf
# This file is a part of Homework_test_environment
#

txt = 'love loves to love love.'

# 数据整理
txt = txt.replace('.', '')
ls = txt.split()

# 计数

d = {}
for i in ls:
    if len(i)>=3: #过滤长度小于3的词
        d[i] = d.get(i, 0) + 1

# 排序（按次数降序）

items = list(d.items())
items.sort(key=lambda x: x[1], reverse=True)

# 输出数据

for i in items[0:2]:
    # print("{}   {}".format(i[0], i[1]))
    print("{}".format(i[0]),end=',')
print('\b。')
