# Code written by gongfuture in 2023.2.19

from turtle import *

setup(650, 350, 200, 200)

penup()
fd(200)
pendown()
pensize(25)
pencolor("purple")
fd(40 * 2 / 3)
circle(-16, 180)
fd(40)
circle(-40, 80 / 2)

for i in range(4):
    circle(40, 80)
    circle(-40, 80)
done()
