"""
Created on:1/21/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to remove specific elements in a numpy array. 

Expected Output:
Original array: 
[ 10 20 30 40 50 60 70 80 90 100]
Delete first, fourth and fifth elements:
[ 20 30 60 70 80 90 100]
"""

import numpy as np
a1=np.array([10,20,30,40,50,60,70,80,90,100])
index=[0,4,5]
a2=np.delete(a1,index)
print(a2)
