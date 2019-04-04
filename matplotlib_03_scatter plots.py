#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [1, 2, 4, 3, 2, 5, 6, 7]

plt.scatter(x, y, label = 'skitscat', color='k', marker='1', s=500) # s=10 定义markersize



# 定义图标横竖轴标签，图标名称
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interestinng Graph\ncheck it out')

# 用于显示数据标签名称
plt.legend()

plt.show()