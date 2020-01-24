'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
problem statement:
Write a Python program to create bar plots with errorbars on the same figure. Attach a text label above each bar displaying men means (integer value).
Sample Date
Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824
Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645
'''
from matplotlib import pyplot as plt
from matplotlib import patches 
import numpy as np

mean=[0.2474, 0.1235, 0.1737, 0.1824]
deviation=[0.3314, 0.2278, 0.2836, 0.2645]
index=np.arange(len(mean))

figure,axis=plt.subplots()

bars=axis.bar(index,mean,0.35,yerr=deviation, color="blue")
plt.xlabel("Velocity")
plt.ylabel("Score")
plt.title("Bar plots with error bars and label")
plt.legend(handles=[patches.Patch(color="gray",label='Men')])
for bar in bars:
    axis.text(bar.get_x()+bar.get_width()/2.,1*(bar.get_height()), "%f" %(bar.get_height()))
plt.minorticks_on()
plt.show()
