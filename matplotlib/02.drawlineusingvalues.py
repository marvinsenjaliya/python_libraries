"""
Created on 1/23/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to draw a line using given axis values with suitable label in the x axis , y axis and a title
"""

from matplotlib import pyplot as plt
x=[1,2,3]
y=[5,6,1]
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('line')
plt.plot(x,y)
plt.show()
