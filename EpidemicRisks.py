# -*- coding: utf-8 -*-
"""
Python adaptation of Matlab code and concept from Dr. Weirtz at Georgia Tech.

https://mobile.twitter.com/joshuasweitz/status/1238173915899293696?fbclid=IwAR2v9x-Ih8o7L45c6BnODB1PbVaNrQVU2w-LWlcPD8DLmNyVu48Ak8Y_viA

Github Repository: https://github.com/jsweitz/covid-19-event-risk-planner/

"""

import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import matplotlib.ticker as ticker
#from matplotlib.ticker import ScalarFormatter
import numpy as np


#setup variables for later use
n=np.logspace(1,5,100)
#population and location
location = 'USA'
pop = 330*10**6
#Tennessee
#location = 'Tennessee'
#pop = 6.77*10**6
#St. Louis
location = 'Knox County'
pop = 461860

#percent risk toleration
risk_vals = [0.01, 0.02, 0.1, 0.5, 0.9]

#set-up plot and axes
fig, ax = plt.subplots()
ax.axis([10,100000,10,pop])

#risk is e~1-(1-p_i)^n where p_i = I/(pop) and n is event size

#draw risk lines
for i in range(len(risk_vals)):
    pcrit_risk = 1 - (1-risk_vals[i])**(1.0/n)
    plt.loglog(n,pcrit_risk*pop, label=(str(risk_vals[i]*100) + ' % Chance'))
    
ax.legend()
#format axis to non-scientific notation below 1 million
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:g}'.format(y)))



#fill below the 1 percent line    
plt.fill_between(n, (1 - (1-risk_vals[0])**(1.0/n))*pop, color='lightgrey')
box_text = ' Less than 1% \n chance of COVID-19 \n positive attendee at the event'
text_box = AnchoredText(box_text, frameon=False, loc=3, pad = 0.5)
plt.setp(text_box.patch, facecolor = 'white', alpha = 0.5)
ax.add_artist(text_box)

#print labels
plt.ylabel('Active circulating infections in ' +location +' , $I$')
plt.xlabel('Number of participants at given event \n Risk is $\epsilon$~1-(1-$p_i$)$^n$ where $p_i$ = $I/(pop)$ and n is event size')
plt.title('Chance of a COVID-19 positive participant at an event in '+ location +' \n\n Assumes Incidence Homogeneity in a population of '+str(pop))
plt.grid(True)
