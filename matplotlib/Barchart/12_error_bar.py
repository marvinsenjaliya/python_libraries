'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
problem statement:
 Write a Python program to create bar plots with error bars on the same figure. Sample Date
Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824
Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645
'''
from matplotlib import pyplot as plt
import numpy as np

mean=[0.2474, 0.1235, 0.1737, 0.1824]
deviation=[0.3314, 0.2278, 0.2836, 0.2645]
index=np.arange(len(mean))

plt.bar(index,mean,0.35,yerr=deviation, color="blue")
plt.xlabel("Velocity")
plt.ylabel("Score")
plt.title("Bar plots with error bars")
plt.minorticks_on()
plt.show()
