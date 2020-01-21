"""
Created on:1/21/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to convert a list and tuple into arrays. 
List to array:
[1 2 3 4 5 6 7 8] 
Tuple to array:
[[8 4 6] 
[1 2 3]]
"""

import numpy as np
list=[1,2,3,4,5,6,7,8]
tuple=((8,4,6),(1,2,3))
a=np.array(list,dtype=int)
print(a)
a=np.array(tuple,dtype=int)
print(a)
