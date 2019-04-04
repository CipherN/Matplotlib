#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import matplotlib.dates as mdates
import datetime as dt


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'label' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                                      delimiter=',',
                                                                      unpack=True,
                                                                      converters={0: bytespdate2num('%Y-%m-%d')}
                                                                      )

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    ax1.plot_date(date, closep, '-', label='Price')

    # 定义数据说明标签的格式
    ax1.plot([], [], linewidth=5, label='Gain', color='g',alpha=0.5)
    ax1.plot([], [], linewidth=5, label='Loss', color='r',alpha=0.5)

    # ax1.fill_between(date, closep[0], closep)
    ax1.fill_between(date, closep[0], closep, where=(closep > closep[0]), facecolor='g', alpha=0.5)
    ax1.fill_between(date, closep[0], closep, where=(closep < closep[0]), facecolor='r', alpha=0.5)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(0)

    ax1.grid(True) #, color='m', linestyle='-', linewidth=1)
    ax1.xaxis.label.set_color('r')
    ax1.yaxis.label.set_color('c')
    ax1.set_yticks([0, 200, 400, 600])

    plt.title(stock)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.subplots_adjust(left=0.09, right=0.94, bottom=0.20, top=0.90, wspace=0.2, hspace=0)
    plt.show()

graph_data('TSLA')

