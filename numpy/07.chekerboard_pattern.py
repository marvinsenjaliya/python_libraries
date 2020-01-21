"""
Created on :1/21/2020
@author:Marvin Senjaliya
"""

"""
problem statement:Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern. 
Checkerboard pattern:
[[0 1 0 1 0 1 0 1] 
[1 0 1 0 1 0 1 0] 
[0 1 0 1 0 1 0 1] 
[1 0 1 0 1 0 1 0] 
[0 1 0 1 0 1 0 1] 
[1 0 1 0 1 0 1 0] 
[0 1 0 1 0 1 0 1] 
[1 0 1 0 1 0 1 0]]
"""

import numpy as np
a=np.ones((3,3))
print(a)
a=np.zeros((8,8),dtype=int)
a[1::2,::2]=1
a[::2,1::2]=1
print(a)
