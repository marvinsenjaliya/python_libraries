"""
Created on :1/21/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to create an array of (3, 4) shape, multiply every element value by 3 and display the new array. 
Expected Output:
Original array elements: 
[[ 0 1 2 3] 
[ 4 5 6 7] 
[ 8 9 10 11]] 
New array elements:
[[ 0 3 6 9] 
[12 15 18 21] 
[24 27 30 33]]
"""

import numpy as np
a1=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
a1.reshape(3,4)
print(a1*3)
 
