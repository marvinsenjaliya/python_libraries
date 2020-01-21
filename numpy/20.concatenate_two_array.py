"""
Created on:1/21/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to concatenate two 2-dimensional arrays. 
Expected Output:
Sample arrays: ([[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]]
Expected Output:
[[ 0 1 3 0 2 4]
[ 5 7 9 6 8 10]
"""

import numpy as np
a1=np.array([[0,1,3],[5,7,9]])
a2=np.array([[0,2,4],[6,8,10]])
c=np.concatenate((a1,a2),axis=0)
print(c)

