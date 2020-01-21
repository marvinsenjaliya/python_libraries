"""
Created on :1/21/2020
@author:Marvin Senjaliya
"""
"""
problem statement:
Write a Python program to create a 3-D array with ones on a diagonal and zeros elsewhere. 
Expected Output:
[[ 1. 0. 0.]
[ 0. 1. 0.] 
[ 0. 0. 1.]]
"""
import numpy as np
a1=np.zeros([3,3],dtype=np.float)
np.fill_diagonal(a1, 1)
print(a1)

