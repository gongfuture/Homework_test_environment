#

# 做直方图

import turtle as t

ls = [69, 292, 33, 131, 61, 254, 500]  # 数据列表
x = len(ls)
y = max(ls)
A_len = 25  # 数据轴宽度
between_len = 50  # 数据轴之间间距
X_len = (A_len + between_len) * x + between_len  # X轴长度
Y_len = y * 1.2  # Y轴长度
x0 = -(X_len / 2)
y0 = -(Y_len / 2)  # 原点相对位置

t.penup()
t.goto(x0, y0)
t.pendown()  # 移动至原点开始作图

t.fd(X_len)
t.fd(-X_len)
t.seth(90)
t.fd(Y_len)  # 画出坐标轴
t.goto(x0, y0)

for i in range(len(ls)):  # 读取数据作图
    t.penup()
    t.seth(0)
    t.fd(between_len)
    t.seth(90)
    t.pendown()
    t.pensize(1)
    t.begin_fill()
    t.color('black', 'red')
    t.fd(ls[i])
    t.seth(0)
    t.fd(A_len)
    t.seth(-90)
    t.fd(ls[i])
    t.end_fill()
t.done()
