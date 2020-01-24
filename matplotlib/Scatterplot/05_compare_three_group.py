'''
Created on 23/01/2020
@author:Marvin Senjaliya
'''
'''
Problem statement:
Write a Python program to draw a scatter plot for three different groups camparing weights and heights
'''
from matplotlib import pyplot as plt
import numpy as np

weight1=np.random.randint(1,60,20)
weight2=np.random.randint(1,60,20)
weight3=np.random.randint(1,60,20)

height1=np.random.randint(1,240,20)
height2=np.random.randint(1,240,20)
height3=np.random.randint(1,240,20)

plt.scatter(weight1,height1,label="group1",color="red")
plt.scatter(weight2,height2,label="group2",color="blue")
plt.scatter(weight3,height3,label="group3",color="green")

plt.

