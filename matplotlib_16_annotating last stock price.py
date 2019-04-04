#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
from matplotlib import style

import numpy as np
import urllib
import datetime as dt

style.use('fivethirtyeight')

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

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

    x = 0
    y = len(date)
    ohlc = []
    while x < y:
        append_me = date[x], closep[x], highp[x], lowp[x], openp[x], volume[x]
        ohlc.append(append_me)
        x+=1

    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)

    ## Method1: add annotation
    # font_dict = {'family':'serif',
    #              'color':'darkred',
    #              'size':15
    #              }
    # ax1.text(date[10], closep[1], 'Text Example', fontdict=font_dict)

    # Method2: add annotation
    # ax1.annotate('Bad News!',
    #              (date[9], closep[9]),
    #              xytext=(0.8,0.9),          # 定义text在图中的位置，x轴在80%，y轴在90%
    #              textcoords='axes fraction',# 同上，定义位置的标记方式，此处以分数表示
    #              arrowprops=dict(facecolor='m')
    #              )

    bbox_props = dict(boxstyle='round',
                      fc='w',
                      ec='k',
                      lw=1
                      )

    ax1.annotate(str(closep[-1]),
                 (date[-1], closep[-1]),
                 xytext=(date[-1]+3, closep[-1]),
                 bbox=bbox_props
                 )

    plt.title(stock)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.subplots_adjust(left=0.09, right=0.94, bottom=0.20, top=0.90, wspace=0.2, hspace=0)
    plt.show()

graph_data('TSLA')

