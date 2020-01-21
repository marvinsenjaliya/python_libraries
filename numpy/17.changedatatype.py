"""
Created on:1/21/2020
@author:Marvin Senjaliya
"""

"""
 Write a Python program to change the data type of an array. 
Expected Output:
[[ 2 4 6]
[ 6 8 10]] 
Data type of the array x is: int32 
New Type: float64 
[[ 2. 4. 6.] 
[ 6. 8. 10.]]

"""

import numpy as np
a1=np.array([2,4,6])
a2=np.array([6,8,10])
b=np.array(a1,dtype=np.float64)
print(b)



























