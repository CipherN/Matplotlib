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


MA1 = 10
MA2 = 30


def moving_average(value, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(value, weights, 'valid')
    return smas


def high_minus_low(highs, lows):
    return highs - lows


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):

    fig = plt.figure()

    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
    plt.title(stock)
    plt.ylabel('H-L')

    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1, sharex=ax1)
    plt.ylabel('Price')
    ax2v = ax2.twinx()

    ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
    plt.ylabel('MAvgs')

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
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x+=1
    ma1 = moving_average(closep, MA1)
    ma2 = moving_average(closep, MA2)
    start = len(date[MA2-1:])

    h_l = list(map(high_minus_low, highp, lowp))
    ax1.plot_date(date, h_l, '-', label='H-L', linewidth=2)
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='lower'))


    candlestick_ohlc(ax2, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')

    ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7, prune='upper'))
    ax2.grid(True)

    bbox_props = dict(boxstyle='round',
                      fc='w',   # facecolot
                      ec='k',   # edgecolor
                      lw=1      # linewidth
                      )

    ax2.annotate(str(closep[-1]),
                 (date[0], closep[0]),
                 xytext=(date[0], closep[0]),
                 bbox=bbox_props
                 )
    ax2v.plot([], [], color='#0079a3', alpha=0.4, label='Volume')
    ax2v.fill_between(date[-start:], 0, volume[-start:], facecolor='#0079a3', alpha=0.4)
    ax2v.axes.yaxis.set_ticklabels([])
    ax2v.grid(False)
    ax2v.set_ylim(0, 0.9*volume.max())

    ax3.plot(date[-start:], ma1[-start:], label=(str(MA1)+'MA'), linewidth=1.5)
    ax3.plot(date[-start:], ma2[-start:], label=(str(MA2)+'MA'), linewidth=1.5)
    ax3.fill_between(date[-start:], ma1[-start:], ma2[-start:],
                     where=(ma1[-start:] < ma2[-start:]),
                     facecolor='r',
                     edgecolor='r',
                     alpha=0.5)
    ax3.fill_between(date[-start:], ma1[-start:], ma2[-start:],
                     where=(ma1[-start:] > ma2[-start:]),
                     facecolor='g',
                     edgecolor='g',
                     alpha=0.5)
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))

    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.subplots_adjust(left=0.11, right=0.90, bottom=0.24, top=0.90, wspace=0.2, hspace=0)

    ax1.legend()
    leg = ax1.legend(loc=9, ncol=2, prop={'size':11})
    leg.get_frame().set_alpha(0.4)

    ax2v.legend()
    leg = ax2v.legend(loc=9, ncol=2, prop={'size': 11})
    leg.get_frame().set_alpha(0.4)

    ax3.legend()
    leg = ax3.legend(loc=9, ncol=2, prop={'size': 11})
    leg.get_frame().set_alpha(0.4)


    plt.show()
    fig.savefig('TSLA.png', facecolor=fig.get_facecolor())

graph_data('TSLA')

