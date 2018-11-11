# -*- coding: utf-8 -*-
"""
Created on Sat May 12 19:45:06 2018

@author: Dev
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 11 17:29:27 2018

@author: Dev
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sunpharma.csv', index_col=0, parse_dates = True)

plt.figure(figsize=(9,9))
plt.subplot(212)
plt.plot(data['Sun'],lw=1, color='red', label ='Sun Pharma stock price')


plt.annotate('FDA accepts filing for new drug',ha = 'center', va = 'bottom',xytext = ('12/26/2017', 550.95),xy = ('12/28/2017', 577.7),
arrowprops = {'facecolor' : 'green', 'shrink' : 0.05, 'headwidth': 10}, )
#

plt.annotate('Bad Q2, but inline with expectations',ha = 'left', va = 'bottom',xytext = ('11/15/2017', 512),xy = ('11/16/2017', 507),
arrowprops = {'facecolor' : 'YELLOW', 'shrink' : 0.05, 'headwidth': 10}, )


plt.annotate('Q3 Profit falls 75%',ha = 'center', va = 'bottom',xytext = ('02/15/2018', 575),xy = ('02/17/2018', 561),
arrowprops = { 'facecolor' : 'red', 'shrink' : 0.05, 'headwidth': 10 })
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
plt.xlim('11/10/2017', '25/02/2018')




