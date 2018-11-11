# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:48:57 2018

@author: Dev
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 11 17:29:27 2018

@author: Dev
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('alkem.csv', index_col=0, parse_dates = True)

plt.figure(figsize=(9,9))
plt.title('NIFTY Pharma Vs NIFTY')

plt.subplot(212)
plt.plot(data['Alkem'],lw=1, color='red', label ='Alkem stock price')

#23th April
plt.annotate('FDA issues 13 observations',ha = 'center', va = 'bottom',xytext = ('03/27/2018', 2093.6),xy = ('03/28/2018', 1988.35),
arrowprops = {'facecolor' : 'red', 'shrink' : 0.05, 'headwidth': 10}, )


plt.grid(True)
plt.legend(loc=0)
plt.xticks(rotation=35)
plt.axis('tight')

plt.xlim('03/12/2018', '04/03/2018')





