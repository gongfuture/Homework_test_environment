# Code written by gongfuture in 2023.2.26

from datetime import datetime

now = datetime.now()
date_ac = int(now.strftime("%Y%m%d"))  # 将日期从str转换成int
print('请输入您的姓名', end="：")
name = input()  # 输入
name_ls = list(name)  # 转换成列表
name_total = 0
for i in range(len(name_ls)):
	name_ls[i] = ord(name_ls[i])  # 逐字转换成Unicode
	name_total = name_total + name_ls[i]
# print(name_ls)
total = date_ac + name_total
# print(total)
print("您今日的幸运数字是：{}".format(total % 100))
