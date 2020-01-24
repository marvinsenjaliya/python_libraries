'''
Created on 23/01/2020
@author:Marvin Senjaliya
'''
'''
Problem statement:
Write a Python program to draw a scatter plot with empty circles taking a random distribution in X and Y and plotted against each other. 
'''
from matplotlib import pyplot as plt
import numpy as np

x=np.random.rand(100)
y=np.random.rand(100)
plt.scatter(x,y,facecolor='none',edgecolor='blue')
plt.show()
