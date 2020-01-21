"""
Created on : 1/21/2020
@author :Marvin Senjalliya
"""

"""
problem statement : Write a Python program to create a null vector of size 10 and update sixth value to 11. 
[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] 
Update sixth value to 11 
[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
"""

import numpy as np
a=np.zeros(10)
print(a)
a[6]=11
print(a)

