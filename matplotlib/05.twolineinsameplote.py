"""
Created on:1/23/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to plot two or more lines on same plot with suitable legends of each line.
"""

from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x=[1,2,3]
y=[4,5,6]
x1=[3,4,5]
y1=[7,8,9]
plt.title('Graph')
plt.xlabel('X-axis')
plt.ylabel('y-axis')
plt.plot(x,y,'g',label='lineone',linewidth=5)
plt.plot(x1,y1,'c',label='linetwo',linewidth=5)
plt.legend()
plt.grid(True,color='k')
plt.show()
