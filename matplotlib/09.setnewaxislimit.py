"""
Created on : 1/23/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
. Write a Python program to display the current axis limits values and set new axis values. 
"""
from matplotlib import pyplot as plt
X=range(1,50)
Y=[value * 3 for value in X]
plt.plot(X,Y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('line')
print(plt.axis())
plt.axis([0,100,0,200])
plt.show()
