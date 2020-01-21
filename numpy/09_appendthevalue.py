"""
Created on:1/21/2020
@author : Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to append values to the end of an array. 
Expected Output:
Original array:
[10, 20, 30] 
After append values to the end of the array:
[10 20 30 40 50 60 70 80 90]

"""

import numpy as np
a=[10 ,20, 30]
a=np.append(a,[40,50,60,70])
print(a)
