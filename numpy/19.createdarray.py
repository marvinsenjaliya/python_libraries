"""
Created on:1/21/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to create an array which looks like below array. 
Expected Output:
[[ 0. 0. 0.]
[ 1. 0. 0.]
[ 1. 1. 0.]
[1. 1. 1.]]
"""
import numpy as np
a1=np.zeros([3,4],dtype=np.float)
print(np.fill_diagonal(a1,1))
print(np.fill_diagonal(a1,1))



