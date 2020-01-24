'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
Problem statement:
Write a Python program to draw a scatter plot using random distributions to generate balls of different sizes. 
'''
from matplotlib import pyplot as plt
import numpy as np

x=np.random.rand(25)
y=np.random.rand(25)
colors=np.random.randint(1,4,25)
areas=np.pi*np.random.randint(5,15,25)**2
plt.scatter(x,y,s=areas,c=colors,alpha=0.85)
plt.show()

