"""
Created on:1/23/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to plot several lines with different format styles in one command using arrays. 
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
x=[1,2,3,4,5,6]
plt.title('line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
style.use('classic')
style.use('ggplot')
plt.plot(x)
plt.show()


