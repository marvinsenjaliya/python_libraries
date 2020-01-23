"""
Created on :1/23/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to plot quantities which have an x and y position.
"""

import numpy as np
import pylab as pl
x1=[2,3,5,6,8]
y1=[1,5,10,18,20]
x2=[3,4,6,7,9]
y2=[2,6,11,20,22]
pl.axis([0,10,0,30])
pl.plot(x1,y1,'b*',x2,y2,'ro')
pl.show()

