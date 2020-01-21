"""
Created on:1/21/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to find the set exclusive-or of two arrays. Set exclusive-or will return the sorted, unique values that are in only one (not both) of the input arrays. 
Array1: [ 0 10 20 40 60 80] 
Array2: [10, 30, 40, 50, 70] 
Unique values that are in only one (not both) of the input arrays: 
[ 0 20 30 50 60 70 80]
"""

import numpy as np
a1=np.array([0,10,20,40,60,80])
a2=np.array([10,30,40,50,70])
np.append(a1,a2)
g=np.intersect1d(a1,a2)
f=np.delete(a1,g)
print(np.sort(f))
