"""
Created on 1/23/2020
@author :Marvin Senjaliya
"""

"""
problem statement :
 Write a Python program to draw a line with suitable label in the x axis, y axis and a title
"""

from matplotlib import pyplot as plt
x=[1,2,3]
y=[4,5,6]
plt.title('line')
plt.xlabel('X-axis')
plt.ylabel('y-axis')
plt.plot(x,y)
plt.show()
