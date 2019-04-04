#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

population_ages = [9, 55, 66, 11, 9, 34, 43, 100, 120, 130, 111, 115, 80, 90, 40, 42, 48, 43]
bins = [0, 10, 30, 60, 70, 80, 100]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)


# 定义图标横竖轴标签，图标名称
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interestinng Graph\ncheck it out')

plt.show()