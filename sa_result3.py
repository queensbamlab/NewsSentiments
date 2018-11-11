# -*- coding: utf-8 -*-
"""
Created on Sat May 12 20:23:20 2018
@author: Dev
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('drreddy.csv', index_col=0, parse_dates = True)

plt.figure(figsize=(9,9))
plt.subplot(212)
plt.plot(data['DRL'],lw=1, color='red', label ='Dr Reddy stock price')

plt.annotate('Mixed Q3, FDA issues',ha = 'center', va = 'bottom',xytext = ('01/29/2018', 550.95),xy = ('04/11/2018', 577.7),
arrowprops = {'facecolor' : 'green', 'shrink' : 0.05, 'headwidth': 10}, )

plt.annotate('Bad Q2, but inline with expectations',ha = 'left', va = 'bottom',xytext = ('11/15/2017', 512),xy = ('11/16/2017', 507),
arrowprops = {'facecolor' : 'YELLOW', 'shrink' : 0.05, 'headwidth': 10}, )


plt.grid(True)
plt.legend(loc=0)
plt.xticks(rotation=35)
plt.axis('tight')
plt.xlim('11/10/2017', '25/02/2018')

