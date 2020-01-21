"""
Created on :1/21/2020
@author :Marvin Senjaliya
"""


"""
problem statement:Write a Python program to convert a list of numeric value into a one-dimensional NumPy array.  
Expected Output:
Original List: [12.23, 13.32, 100, 36.32] 
One-dimensional numpy array: [ 12.23 13.32 100. 36.32] 
"""
import numpy as np 
my_list = [1, 3, 5, 7, 9] 
  
print ("Input  list : ", my_list) 
out_arr = np.asarray(my_list) 
print ("output array from input list : ", out_arr)  
