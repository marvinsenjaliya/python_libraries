"""
Created on 1/23/2020
@author :Marvin Senjaliya
"""

"""
problem statement:
 Write a Python program to plot two or more lines and set the line markers. 
"""


from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x=[1,2,3]
y=[5,6,1]
x1=[3,4,5]
y1=[7,8,1]
plt.title('line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x,y,'g',label='lineone',linewidth=5,
markersize=12)
plt.plot(x,y,'c',label='linetwo',linewidth=5,
markersize=12)
plt.legend()
plt.show()
