#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import matplotlib.pyplot as plt

# 数据
days = [1, 2, 3, 4, 5]

sleeping = [5, 6, 7, 3, 4]
eating = [8, 5, 5, 8, 3]
working = [2, 3, 4, 3, 4]
playing = [1,3,4,6,4]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.2,0,0),
        autopct='%1.1f%%',  # 1.2f% 表示保留两位小数，如29.22%
        )

# 定义图标横竖轴标签，图标名称
# plt.xlabel('x')
# plt.ylabel('y')
plt.title('Interestinng Graph\ncheck it out')

# 用于显示数据说明标签名称
# plt.legend()

# 显示图片
plt.show()