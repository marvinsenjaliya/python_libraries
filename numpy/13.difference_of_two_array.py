"""
Created on :1/21/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to find the set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2. 
Expected Output:
Array1: [ 0 10 20 40 60 80]
Array2: [10, 30, 40, 50, 70, 90] 
Set difference between two arrays:
[ 0 20 60 80]
"""

import numpy as np
a1=np.array([0,10,20,40,60,80])
a2=np.array([10,30,40,50,70,80])
np.append(a1,a2)
g=np.intersect1d(a1,a2)
print(np.delete(a1,g))
print(g)
