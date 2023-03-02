# Code written by Qian Jinli and modified by gongfuture in 2023.2.20

from turtle import *  # 引用turtle库至全局

# speed(1)    # 测试用，更改绘画速度
pendown()
begin_fill()
color('black', 'black')
circle(-90, -180)
seth(0)
circle(180, 180)
end_fill()  # 画出大片黑色部分
home()
begin_fill()
color('white', 'white')
circle(90, 180)
end_fill()  # 画出大片白色部分
left(90)
penup()
fd(90)
pendown()
dot(30, 'Black')  # 画出黑点
penup()
home()
right(90)
penup()
fd(90)
pendown()
dot(30, 'white')  # 画出白点
penup()
color('black')
goto(0, 180)
seth(0)
pendown()
pensize(3)
circle(-180)  # 画出外框
