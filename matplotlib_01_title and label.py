#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3]
y = [7, 2, 9]

x2 = [1, 2, 3]
y2 = [10, 20,2]

# 定义数据标签
plt.plot(x, y, label = "First one")
plt.plot(x2, y2, label = "Second one")

# 定义图标横竖轴标签，图标名称
plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.title('Interestinng Graph\ncheck it out')

# 用于显示数据标签名称
plt.legend()
plt.show()