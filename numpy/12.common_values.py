"""
Created on:1/21/2020
@author:Marvin Senjaliya
"""


"""
problem statement:
Write a Python program to find common values between two arrays. 
Expected Output:
Array1: [ 0 10 20 40 60] 
Array2: [10, 30, 40]
Common values between two arrays:
[10 40] 
"""

import numpy as np
a1=np.array([0, 10, 20, 40, 60])
a2=np.array([10, 30, 40])
print(np.intersect1d(a1,a2))

