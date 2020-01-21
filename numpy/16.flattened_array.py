"""
Created on :1/21/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to create a contiguous flattened array. 
Original array:
[[10 20 30] 
[20 40 50]] 
New flattened array: 
[10 20 30 20 40 50]
"""

import numpy as np
a1=np.array([10,20,30])
a2=np.array([20,40,50])
print(np.append(a1,a2))
