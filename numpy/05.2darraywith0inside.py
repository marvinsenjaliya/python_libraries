"""
Created on:1/21/2020
@author:Marvin Senjaliya
"""

"""
problem statement:

5. Write a Python program to create a 2d array with 1 on the border and 0 inside.  
Expected Output:
Original array: 
[[ 1. 1. 1. 1. 1.] 
[ 1. 1. 1. 1. 1.] 
[ 1. 1. 1. 1. 1.] 
[ 1. 1. 1. 1. 1.] 
[ 1. 1. 1. 1. 1.]] 
1 on the border and 0 inside in the array 
[[ 1. 1. 1. 1. 1.] 
[ 1. 0. 0. 0. 1.] 
[ 1. 0. 0. 0. 1.] 
[ 1. 0. 0. 0. 1.] 
[ 1. 1. 1. 1. 1.]]
"""

import numpy as np
a=np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],dtype=float)
print(a)
a[1:4,1:4]=0
print(a)
