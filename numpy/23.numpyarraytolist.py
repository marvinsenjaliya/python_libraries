"""
Created on:1/21/2020
@author:Marvin Senjaliya
"""

"""
problem statement:

23. Write a Python program to convert a NumPy array into Python list structure. 
Expected Output:
Original array elements:
[[0 1]
[2 3] 
[4 5]] 
Array to list: 
[[0, 1], [2, 3], [4, 5]]
"""

import numpy as np
a1=np.array([[0, 1],[2, 3],[4, 5]])
a2=a1.tolist()
print(a2)
