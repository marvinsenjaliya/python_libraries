"""
Created on:1/23/2020
@author:Marvin Senjaliya
""" 

"""
problem statement:
Write a Python program to plot two or more lines with legends, different widths and colors. 
"""
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x=[1,2,3]
y=[4,5,1]
x1=[7,8,9]
y1=[10,11,1]
plt.title('lines')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x,y,'g',label='lineone',linewidth=5)
plt.plot(x1,y1,'c',label='lineone',linewidth=10)
plt.legend()
plt.grid(True,color='k')
plt.show()

