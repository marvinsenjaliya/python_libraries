"""
Created on:1/21/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
. Write a Python program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements. 
Expected Output:
Size of the array: 3
Length of one array element in bytes: 8 
Total bytes consumed by the elements of the array: 24
"""
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
print(np.size(a))
print(a.itemsize)
print(a.nbytes)

