# -*- coding: utf-8 -*-
"""
Created on Fri May 11 17:29:27 2018

@author: Dev
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Lupin.csv', index_col=0, parse_dates = True)

plt.figure(figsize=(9,9))
plt.title('NIFTY Pharma Vs NIFTY')

plt.subplot(212)
plt.plot(data['Lupin'],lw=1, color='red', label ='Lupin stock price')

#23th April
plt.annotate('FDA approval on Xenazine tablets',ha = 'center', va = 'bottom',xytext = ('04/20/2018', 811.85),xy = ('04/24/2018', 819.75),
arrowprops = {'facecolor' : 'green', 'shrink' : 0.05, 'headwidth': 10}, )

#6th April
plt.annotate('EIR from FDA for Pithampur unit',ha = 'center', va = 'bottom',xytext = ('04/04/2018', 786.7),xy = ('04/06/2018', 809.05),
arrowprops = {'facecolor' : 'green', 'shrink' : 0.05, 'headwidth': 10}, )

#8th May
plt.annotate('FDA approval for skin drug',ha = 'center', va = 'bottom',xytext = ('05/06/2018', 774.85),xy = ('05/08/2018', 786),
arrowprops = { 'facecolor' : 'green', 'shrink' : 0.05, 'headwidth': 10 })
#
## 10th Nov
#plt.annotate('Trumps "Make in US" News Worries the Sector',ha = 'center', va = 'bottom',xytext = ('11/9/2016', 11325),xy = ('11/10/2016', 10990.6),
#arrowprops = { 'facecolor' : 'black', 'shrink' : 0.05 })
#
## 16 nov
#plt.annotate('Rising US Approvals News',ha = 'center', va = 'bottom',xytext = ('11/15/2016', 10950),xy = ('11/16/2016', 10559.3),
#arrowprops = { 'facecolor' : 'black', 'shrink' : 0.05 })

plt.grid(True)
plt.legend(loc=0)
plt.xticks(rotation=35)
plt.axis('tight')
plt.ylim(730,830)
plt.xlim('03/25/2018', '05/09/2018')




