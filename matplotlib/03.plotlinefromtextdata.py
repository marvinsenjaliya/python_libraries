"""
Created on 1/23/2020
@author:Marvin Senjaliya
"""
 
"""
problem statement:
 Write a Python program to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title.
Test Data:
test.txt
1 2
2 4
3 1
"""
from matplotlib import pyplot as plt

x,y = [] ,[]
for line in open('test.txt','r'):
	values=[float(s) for s in line.split()]
	x.append(values[0])
	y.append(values[1])
plt.plot(x,y)
plt.show()
