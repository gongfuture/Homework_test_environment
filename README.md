# 个人课程作业存档

---

## 前言

* 这里记录了我个人上的Python课程和Web课程的作业需求以及成品 ~~欢迎同学来抄（bushi）~~
* 但同时，也是我个人学习Python的记录，也因为这个契机，学习了Markdown语法和Git的用法
  ~~这个文档之后多半也会当一块试验田吧~~
* 这个README已经写的有些繁琐了,正在考虑用什么东西自动管理它

## 正文

[点击这里跳转到Web作业](#web作业)

### Python作业

| 次数  | 内容                          | 需求                            | 成品                     | 详细内容            |
|:---:|-----------------------------|-------------------------------|------------------------|-----------------|
|  1  | 程序设计与Turtle库初识              | [作业1.txt](Python/作业1/作业1.txt) | [作业1目录](Python/作业1/成品) | [作业1详细内容](#作业1) |
|  2  | 程序设计之表达式应用（I）与Turtle库应用（II） | [作业2.txt](Python/作业2/作业2.txt) | [作业2目录](Python/作业2/成品) | [作业2详细内容](#作业2) |

<!--
| 第三次作业 | [作业3.txt](Python/作业3/作业3.txt) | [作业3目录](Python/作业3/成品) | [作业3详细内容](#py3) |
| 第四次作业 | [作业4.txt](Python/作业4/作业4.txt) | [作业4目录](Python/作业4/成品) | [作业4详细内容](#py4) |
| 第五次作业 | [作业5.txt](Python/作业5/作业5.txt) | [作业5目录](Python/作业5/成品) | [作业5详细内容](#py5) |
| 第六次作业 | [作业6.txt](Python/作业6/作业6.txt) | [作业6目录](Python/作业6/成品) | [作业6详细内容](#py6) |
-->

#### 作业1

需求：[作业1.txt](Python/作业1/作业1.txt)  
成品：位于 [作业1](Python/作业1/成品) 目录下，点击跳转，~~目前共完成(4/5)~~ 第五项已被老师移动至下一次作业
<details>
<summary>详细内容点击展开</summary>
<details>
<summary>作业1需求</summary>

```
实验1 程序设计与Turtle库初识

1、输出任意n边形。

2、首先，读懂下面绘制大蟒蛇的代码，
   然后，将代码改写为，反向输出的大蟒蛇。

#大蟒蛇

from turtle import *
setup(650,350,200,200)

penup()
fd(-250)   #fd(250)
pendown()
pensize(25)
pencolor("purple")
seth(-40)  #set(140)

for i in range(4):
    circle(40,80)
    circle(-40,80)

circle(40,80/2)
fd(40)
circle(16,180)
fd(40*2/3)
done()

3、输出间距和边长都是80的，五个等边四边形

*4、自主设计并输出一个图标（可以是商标、宿舍标、班级标等等）

5、画出指定图形的直方图(直方图，在上课时给出)    #移动至第二次作业


注意：

1、本次作业暂时不上交，但需要妥善保存好调试后的代码，后面再交。

2、第1次实习课，任选以上3条或3条以上的题目。

3、作业所写的代码，可以参考一切可以参考的素材，包括百度。但最终需要自己独立撰写。


服务器：ftp://211.65,95.251
用户名：student_wll
password:student_wll

```

</details>
<details>
<summary>1.输出任意n边形</summary>

```python
# Code written by gongfuture in 2023.2.19

from turtle import *

n = eval(input("请输入需要的边数："))
# speed(1)    # 更改速度测试用
setup(650, 400, 200, 200)
pensize(3)
penup()
goto(50, 50)
pendown()
begin_fill()
color('black')
circle(40, steps=n)
end_fill()

# input()  # 需要暂停时启用
```

</details>
<details>
<summary>2.反向输出的大蟒蛇</summary>

```python
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

```

</details>
<details>
<summary>3.输出间距和边长都是80的，五个等边四边形</summary>

```python
# Code written by gongfuture in 2023.2.20

import turtle

turtle.setup(1000, 400)
turtle.penup()
turtle.pensize(2)
turtle.color("black")
turtle.goto(-400, -50)
turtle.seth(45)
# turtle.speed(1)    #测试使用，减缓动画速度
i = 1
while i < 6:
	turtle.pendown()
	turtle.circle(80 / 2 ** 0.5, steps=4)
	turtle.penup()
	turtle.goto(-400 + 160 * i, -50)
	i = i + 1

```

</details>
<details>
<summary>4.自主设计并输出一个图标（可以是商标、宿舍标、班级标等等）</summary>

```python
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

```

</details>
</details>

#### 作业2

需求：[作业2.txt](Python/作业2/作业2.txt)</br>
成品：位于 [作业2](Python/作业2/成品) 目录下，点击跳转
<details>
<summary>详细内容点击展开</summary>

<details>
<summary>作业2需求</summary>

```
作业2 程序设计之表达式应用（I）与Turtle库应用（II）

1、
试编写代码，完成功能：
输入：出生日期（4位年）
输出：相应的属相。

示例：
输入：2001
输出：你的属相是，蛇


2、
从键盘输入一组数据（字母和数字的组合），编写程序，将输入的字符串反向输出。

示例：
输入：love loves to love love.
输出：.evol evol ot sevol evol


3、
系统提示输入用户姓名，然后编写程序，利用随机函数和适当的算法，为用户输出一个今日的幸运数字。

示例：
输入：请输入您的姓名：王力宏
输出：王力宏今日的幸运数字是，36

4、
输出下面图形。

          1
         222
        33333
       4444444
      555555555

5、
已知做直方图代码如下：
#做直方图

import turtle as t

ls=[69,292,33,131,61,254]
X_len=400
Y_len=300
x0=-200
y0=-100

t.penup()
t.goto(x0,y0)
t.pendown()

t.fd(X_len)
t.fd(-X_len)
t.seth(90)
t.fd(Y_len)


for i in range(len(ls)):
    t.penup()
    t.goto(x0+(i+1)*50,y0 )
    t.seth(90)
    t.pendown()
    t.pensize(8)
    t.pencolor('blue')
    t.fd(ls[i])
t.done()


试着改写上述代码，将直方图的蓝色线改成红色矩形框。图示见QQ群。































































































（1）、下面代码实现功能：从键盘输入一个1-26之间的数字，对应英文小写字母表中的索引，在屏幕上显示输出对应的英文字母。示例如下：
输入：1
输出：a

# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

s=input("请输入：")
print("输出一个字母，{}".format(  chr(eval(s)+96) ))

（2）、请写代码替换横线，不修改其他代码，实现以下功能：从键盘输入一个中文字符串变量s，
内部包含中文逗号和句号。计算字符串s中的中文字符个数，不包括中文逗号和句号字符。
示例如下：
输入：快乐小蜜蜂，飞到东来飞到西，采蜜忙啊采蜜忙。
输出：中文字符数为19。

# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

s=input("请输入一个中文字符串，包含逗号和句号：")
s=s.replace("，",""). replace（"。"，" "）  
m= （len(s)） 
print("\n中文字符数为{}。".format(m ))


（3）、请写代码替换横线，不修改其他代码，实现以下功能：键盘输入字符串s，按要求把s输出到屏幕，
模式要求：宽度为20个字符，等号字符=填充，居中对齐。如果输入字符串超过20位，则全部输出。
例如：键盘输入字符串s为”PYTHON”，屏幕输出=======PYTHON=======。

# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

s = input("请输入一个字符串:")
print("{ :=^20}".format(s))

（4）、请写代码替换横线，不修改其他代码，实现以下功能：
从键盘输入4个数字，各数字采用空格分隔，对应为变量x0,y0,x1,y1。计算两点（x0,y0）
和（x1,y1）之间的距离，屏幕输出这个距离，保留2位小数。
例如：键盘输入：0 1 3 5  屏幕输出：5.00

# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

ntxt = input("请输入4个数字(空格分隔):")
nls=ntxt.split()
x0 = eval(nls[0])
y0 = eval(nls[1])
x1 = eval(nls[2])
y1 = eval(nls[3])
r = pow(pow(x1-x0, 2) + pow(y1-y0, 2), 0.5 ) 
print("{:.2f}".format(r))


（5）、试编写代码，完成功能：
输入：出生日期（4位年）
输出：相应的属相。
示例：
输入：2001
输出：蛇（或巳蛇）

#参考代码

n=eval(input("请输入出生年："))
s="鼠牛虎兔龙蛇马羊猴鸡狗猪"
print("你的属相是，{}".format(s[(n-4)%12]))

```

</details>
<details>
<summary>1.输入生日输出属相</summary>

```python
# Code written by gongfuture in 2023.2.25

birth = eval(input("请输入出生年份（四位年，例：1900）："))
# 天干：年份减3，除以10，没有余数就是天干的最后一个，余数是1对应 甲 ，是2对应 乙 ，依次往后推
# 地支：年份减3，除以12，没有余数就是地支的最后一个，余数是1对应 子 ，是2对应丑，依次往后推。
# 年份÷12求余数 0猴 1鸡 2狗 3猪 4鼠 5牛 6虎 7兔 8龙 9蛇 10马 11羊
tiangan_remain = (birth - 4) % 10
dizhi_remain = (birth - 4) % 12
shengxiao_remain = (birth - 4) % 12
tiangan_list = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhi_list = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
shengxiao_list = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
tiangan = tiangan_list[tiangan_remain]
dizhi = dizhi_list[dizhi_remain]
shengxiao = shengxiao_list[shengxiao_remain]
# print(tiangan_remain,dizhi_remain,shengxiao_remain)
print("您的属相是：{}".format(tiangan + dizhi + shengxiao))

```

</details>
<details>
<summary>2.反向输出字符串</summary>

```python
# Code written by gongfuture in 2023.2.26

print('请输入需要反向输出的字符串', end="：")
b = input()
d = "反向输出的字符串为："
length = len(b)
# print(length)
for i in range(length + 1):
	d = d + b[length - i: length - i + 1]
print(d)

# print('请输入需要反向输出的字符串', end="：")
# b = input()
# d = "反向输出的字符串为："
# ls = list(b)
# ls.reverse()
# for i in range(len(ls)):
# 	d = d + ls[i]
# print(d)

```

</details>
<details>
<summary>3.输入姓名，随机函数，输出今日幸运数字</summary>

```python
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

```

</details>
<details>
<summary>4.输出指定图形</summary>

```python
# Code written by gongfuture in 2023.2.26
# 实在太过简单甚至不想加上面这行（

print("""

          1
         222
        33333
       4444444
      555555555

""")

```

</details>
<details>
<summary>5.上次的直方图</summary>

```python
# Code written by teacher modified and comment out by gongfuture in 2023.2.25

# 做直方图

import turtle as t

ls = [69, 292, 33, 131, 61, 254]  # 数据列表
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
t.goto(x0, y0)
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

```

</details>
</details>
<br>

### Web作业

[点击这里跳转到Python作业](#python作业)

| 次数  | 内容           | 需求                                                                   | 成品                                         | 附件                                               | 详细内容                |
|:---:|--------------|----------------------------------------------------------------------|--------------------------------------------|--------------------------------------------------|---------------------|
|  1  | 文字、列表、图像与超链接 | [第1次作业.txt](Web-Html/第1次作业（文字、列表、图像与超链接）/要求/第1次作业（文字、列表、图像与超链接）.txt) | [第1次作业目录](Web-Html/第1次作业（文字、列表、图像与超链接）/成品) | [第1次作业附件](Web-Html/第1次作业（文字、列表、图像与超链接）/要求/作业1附件) | [第1次作业详细内容](#第1次作业) |

#### 第1次作业

需求：[第1次作业（文字、列表、图像与超链接）.txt](Web-Html/第1次作业（文字、列表、图像与超链接）/要求/第1次作业（文字、列表、图像与超链接）.txt)  
附件：位于[作业1附件](Web-Html/第1次作业（文字、列表、图像与超链接）/要求/作业1附件)目录下，点击跳转  
成品：位于[成品](Web-Html/第1次作业（文字、列表、图像与超链接）/成品)目录下，点击跳转

<details>
<summary>详细内容点击展开</summary>
<details>
<summary>page1</summary>

HtmL

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta content="gongfuture" name="author">
    <link href="page1.css" rel="stylesheet" type="text/css">
    <title>page1</title>
</head>
<body>
<h1>
    关于我们
</h1>
<p><span style="font-size:1.5em;color:red;">五</span>十个不同的分子，在不同状态下进入了同一容器，这就组成了我们的家——<b>计算机应用专业</b>。<i>在这个容器里，我们碰撞着，摩擦着，产生了各色各样的灵感，活力与情绪。</i>
</p>
<p><span style="font-size:1.5em;color:red;">在</span>不地碰撞和摩擦中，分子也不断地变化，成长着，最终可走出这个容器，勇敢地面对、挑战外面的世界。
    不管外面如何复杂、艰难，请大家彼此珍惜这段我们相逢相识相知的日子，在这里我们痛过笑过哭过，不论是苦的还是甜的，这都是我们年轻的见证。
</p>
<p><span style="font-size:1.5em;color:red;">无</span>论以后的日子，你会碰到什么困难，遇到什么坎坷，<span
        style="color:blue">请记住</span>在这里还有另外的四十九份热情和真心支持着，鼓励着你，<span
        style="color:blue">请记住</span>我们是一个团体，不会丢下谁，不会落下谁。共同奋进！！
</p>
<p style="text-align:right;text-decoration:underline;">我们永远的家——计算机应用专业！</p>
<hr style="border: 0.3em solid grey;"/>
<ol start="1" type="1">
    <li><a href="page1.html" title="第一个网页">第一个网页</a></li>
    <li><a href="page2.html" title="第二个网页">第二个网页</a></li>
</ol>
</body>
</html>
```

Css

```css
body{
    background-color:white;
    font-size:100%;
    font-family:"宋体";
}
h1{
    font-size:2.5em;
    color:black;
    text-align:center;
}
p{
    text-indent: 2em;
    color:black;
}

```

</details>
<details>
<summary>page2</summary>

Html

```html
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <meta content="gongfuture" name="author">
    <link href="page2.css" rel="stylesheet" type="text/css">
    <title>page2</title>
</head>
<body>
<h1>
    关于我们
</h1>
<p>五十个不同的分子，</br>
    在不同状态下进入了同一容器，</br>
    这就组成了我们的家——计算机应用专业。</br>
    在这个容器里，我们碰撞着，摩擦着，产生了各色各样的灵感，活力与情绪。<br/></p>
<p style="text-align:right;text-decoration:underline;">我们永远的家——计算机应用专业！</p>
<p><img alt="配图" src="1.jpg"></p>
<hr style="border: 0.3em solid grey;"/>
<ol start="1" type="1">
    <li><a href="page1.html" title="第一个网页">第一个网页</a></li>
    <li><a href="page2.html" title="第二个网页">第二个网页</a></li>
</ol>
</body>
</html>
```

Css

```css
body{
    background-color:white;
    font-size:100%;
    font-family:"宋体";
}
h1{
    font-size:2.5em;
    color:black;
    text-align:center;
}
p{
    text-align:center;
    color:black;
}

```

</details>
</details>

<br><br><br><br><br>

### 以下预留，仅为注释

<!--
详细内容标准格式
#### 作业1</br>
需求：[作业1.txt](Python/作业1/作业1.txt)  
成品：位于 [作业1](Python/作业1/成品) 目录下，点击跳转

<details>
<summary>详细内容点击展开</summary>
<details>
<summary></summary>

```python

```

</details>
</details>
-->