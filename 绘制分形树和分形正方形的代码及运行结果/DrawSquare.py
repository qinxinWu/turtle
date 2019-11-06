# !/usr/bin/env python
# coding:utf-8
# Author: Qingxin Wu

import turtle

#绘制分形正方形的递归方法
#length是指每个正方形边长的长度
def drawFractalSquare(length):
    #限定递归函数终止的条件为：当传入的边长小于等于10时递归终止即只有大于10才能执行
    if length > 10:
        #先是画向上的边：方向为竖直向上
        turtle.forward(length)
        #其次，把画笔的方向向右旋转90度，开始画向右的边
        turtle.right(90)
        turtle.forward(length)
        #接着，把画笔的方向向右旋转90度，开始画向下的边
        turtle.right(90)
        turtle.forward(length)
        # 最后，把画笔的方向向右旋转90度，开始画向左的边
        turtle.right(90)
        turtle.forward(length)
        # 然后，把画笔的方向向右旋转90度调整回竖直向上
        turtle.right(90)
        #开始递归调用绘制右边的正方形
        drawFractalSquare(length-5)


# 由于初始画笔的方向是水平向右的，要先把方向向左方向旋转90度调整为竖直向上
turtle.left(90)
#设置画笔的粗细大小为3
turtle.pensize(3)
#设置画笔的颜色为蓝色
turtle.color('blue')

#此处绘制分形正方形
#开始递归绘制，并给出初始边长长度为50
drawFractalSquare(50)
#使得绘制完成不直接退出，而是点击一下才退出
turtle.exitonclick()








