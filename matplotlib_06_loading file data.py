#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import matplotlib.pyplot as plt

# Part 1
'''
import csv

x = []
y = []

with open('example.txt', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x.append(int(row[0]))
                y.append(int(row[1]))
plt.plot(x, y, label='Loaded from file!')
'''

# Part 2
import numpy as np

x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)

plt.plot(x, y, label='Loaded from file!')

# 定义图标横竖轴标签，图标名称
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interestinng Graph\ncheck it out')

## 用于显示数据标签名称
plt.legend()

# 显示图片
plt.show()
