"""
Created on 1/23/2020
@author:Marvin Senjaliya
"""
"""
problem statement:
write a python program to create multiple plots
"""

from matplotlib import pyplot as plt
#importing matplotlib
import matplotlib.pyplot as plt,numpy as np
# line points
x_axis_line= np.array([10,20,30,70,80,90])
y_axis_line = np.array([20,40,10,23,22,12])
#calling subplot method to create multiple plots/axis
#generating axes
#giving argument as 
#total figure grid,axix of each figure,starting point of each figure,rowspan,colspan
axis_one = plt.subplot2grid((8,8),(0,0),rowspan=2,colspan=2)
axis_two = plt.subplot2grid((8,8),(0,4),rowspan=2,colspan=2)
axis_three = plt.subplot2grid((8,8),(4,0),rowspan=2,colspan=2)
axis_four = plt.subplot2grid((8,8),(4,4),rowspan=2,colspan=2)
#plotting graphs
axis_one.plot(x_axis_line,y_axis_line)
axis_two.plot(x_axis_line*2,y_axis_line)
axis_three.plot(x_axis_line,y_axis_line*2)
axis_four.plot(x_axis_line,y_axis_line*4)

