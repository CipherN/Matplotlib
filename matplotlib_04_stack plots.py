#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import matplotlib.pyplot as plt

# 数据
days =[1, 2, 3, 4, 5]
sleeping =[5,6,7,3,4]
eating =[8,5,5,8,3]
working =[2,3,4,3,4]
playing =[1,3,4,6,4]

# 显示区域标签
plt.plot([], [], label='sleeping', color='m',linewidth=5)
plt.plot([], [], label='eating', color='r',linewidth=5)
plt.plot([], [], label='working', color='c',linewidth=5)
plt.plot([], [], label='playing', color='k',linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'r', 'c', 'k'])


# 定义图标横竖轴标签，图标名称
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interestinng Graph\ncheck it out')

# 用于显示数据标签名称
plt.legend()

# 显示图片
plt.show()