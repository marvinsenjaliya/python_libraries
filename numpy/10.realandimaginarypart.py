"""
Created on :1/21/2020
@author:Marvin Senjaliya
"""
"""
problem statement:
. Write a Python program to find the real and imaginary parts of an array of complex numbers. 
Expected Output:
Original array [ 1.00000000+0.j 0.70710678+0.70710678j] 
Real part of the array: 
[ 1. 0.70710678] 
Imaginary part of the array:
[ 0. 0.70710678] 
"""


import numpy as np
x=np.sqrt([1.00+0.j])
print(x.real)
print(x.imag)

