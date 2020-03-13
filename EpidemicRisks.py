# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import numpy as np


n=np.logspace(1,5,100)
pcrit = 0.01/n
pop = 330*10**6
risk_vals = [0.01, 0.02, 0.1, 0.5, 0.9]

plt.close()
fig, ax = plt.subplots()

#draw risk lines
for i in range(len(risk_vals)):
    pcrit_risk = 1 - (1-risk_vals[i])**(1.0/n)
    plt.loglog(n,pcrit_risk*pop, label=(str(risk_vals[i]*100) + ' % Chance'))
    
ax.legend()
    
plt.fill_between(n, (1 - (1-risk_vals[0])**(1.0/n))*pop, color='lightgrey')

plt.ylabel('Active circulating infections in the USA, $I$')
plt.yticks()
plt.xlabel('Number of participants at given event')
plt.title('Chance of a COVID-19 positive participant at an event \n\n Assumes Incidence Homogeneity')
plt.grid(True)

box_text = 'Less than 1% \n chance of COVID-19 \n positive attendee at the event'
text_box = AnchoredText(box_text, frameon=False, loc=3, pad = 0.5)
plt.setp(text_box.patch, facecolor = 'white', alpha = 0.5)
ax.add_artist(text_box)


# For these scenarios, use the exact risk assuming homogeneity
#for i in range(len(sizevec)):
#   p_equiv = nvec/USpop;
#   eps_equiv(i) = 1-(1-p_equiv).^sizevec(i);
#   tmpt=text(sizevec(i)*(1-0.08*(i-1)),nvec*0.6,sprintf('%3.2g%% chance',eps_equiv(i)*100));