import time
import turtle as t

n = eval(input("请输入需要的边数："))
t.setup(650, 400, 200, 200)
t.pensize(3)
t.penup()
t.goto(50, 50)
t.pendown()
t.begin_fill()
t.color('black')
t.circle(40, steps=n)
t.end_fill()

input()
