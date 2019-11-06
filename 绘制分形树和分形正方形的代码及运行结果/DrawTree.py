# !/usr/bin/env python
# coding:utf-8
# Author: Qingxin Wu

import turtle

#绘制分形树的递归方法
#length是指每个树干的长度
def drawFractalTree(length):
    #限定递归函数终止的条件为：当传入的树干的长度小于等于10时递归终止即只有大于10才能执行
    if length > 10:
        #先是画主树干：方向为竖直向上
        turtle.forward(length)
        #其次，把画笔的方向向右旋转33度，为了接下来画右子树
        turtle.right(33)
        #由于要和实际的树相符，所以一般来说子树干会比主树干长度小，所以我这里设置子树干的长度仅为主树干的0.8倍长
        #且这里开始调用自身函数，即递归开始绘制右子树
        drawFractalTree(0.8 * length)
        #接下来准备画左子树
        #由于此时画笔已经是与竖直方向相比向右偏移了33度，所以为了左右子树对称，此时要将画笔方向向左旋转33度*2，即66度
        turtle.left(66)
        #同理，左子树的树干长度也是主树干的0.8倍，开始递归绘制左子树
        drawFractalTree(0.8 * length)
        # 左子树绘制完成后要返回到原来的竖直方向的主树干上，所以要先向右旋转33度，然后沿袭竖直向下方向返回同样长度
        turtle.right(33)
        turtle.backward(length)





# 由于初始画笔的方向是水平向右的，所以要画竖直向上的树，要先把方向向左方向旋转90度
turtle.left(90)
#设置画笔的粗细大小为3
turtle.pensize(3)
#设置画笔的颜色为蓝色
turtle.color('blue')
#开始递归绘制，并给出初始树干长度为50
drawFractalTree(50)
#使得绘制完成不直接退出，而是点击一下才退出
turtle.exitonclick()









