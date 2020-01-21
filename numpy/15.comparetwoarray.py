"""
Created on :1/21/2020
@author:Marvin Senjaliya
"""


"""
problem statemenet:
 Write a Python program compare two arrays using numpy. 
Array a: [1 2]
Array b: [4 5]
a > b 
[False False]
a >= b 
[False False] 
a < b 
[ True True] 
a <= b 
[ True True]
"""

import numpy as np
a1=np.array([1,2])
a2=np.array([4,5])

print(a1>a2)
print(a1<a2)
print(a1==a2)

