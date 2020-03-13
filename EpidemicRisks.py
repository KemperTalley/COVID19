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
#location = 'USA'
#pop = 330*10**6
#Tennessee
location = 'Tennessee'
pop = 6.77*10**6

#percent risk toleration
risk_vals = [0.01, 0.02, 0.1, 0.5, 0.9]

fig, ax = plt.subplots()
ax.axis([10,100000,10,pop])





#draw risk lines
for i in range(len(risk_vals)):
    pcrit_risk = 1 - (1-risk_vals[i])**(1.0/n)
    plt.loglog(n,pcrit_risk*pop, label=(str(risk_vals[i]*100) + ' % Chance'))
    
ax.legend()

#format the y-axis to be in non-scientific notation
#for axis in [ax.xaxis, ax.yaxis]:
#    formatter = ScalarFormatter()
#    formatter.set_scientific(False)
#    axis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:g}'.format(y)))



#fill below the 1 percent line    
plt.fill_between(n, (1 - (1-risk_vals[0])**(1.0/n))*pop, color='lightgrey')
box_text = '  Less than 1% \n  chance of COVID-19 \n  positive attendee at the event'
text_box = AnchoredText(box_text, frameon=False, loc=3, pad = 0.5)
plt.setp(text_box.patch, facecolor = 'white', alpha = 0.5)
ax.add_artist(text_box)

#print labels
plt.ylabel('Active circulating infections in ' +location +' , $I$')
#plt.yticks(labels=[10,100,1000,10000,100000,1000000])
plt.xlabel('Number of participants at given event')
plt.title('Chance of a COVID-19 positive participant at an event \n\n Assumes Incidence Homogeneity')
plt.grid(True)




# For these scenarios, use the exact risk assuming homogeneity
#for i in range(len(sizevec)):
#   p_equiv = nvec/USpop;
#   eps_equiv(i) = 1-(1-p_equiv).^sizevec(i);
#   tmpt=text(sizevec(i)*(1-0.08*(i-1)),nvec*0.6,sprintf('%3.2g%% chance',eps_equiv(i)*100));