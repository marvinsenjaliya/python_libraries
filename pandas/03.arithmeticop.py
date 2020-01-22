"""
Created on:1/22/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to add, subtract, multiple and divide two Pandas Series.  
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
"""
import pandas as pd
a1=[2,4,6,8,10]
a2=[1,3,5,7,9]
s1=pd.Series(a1)
s2=pd.Series(a2)
sa=s1.add(s2)
ss=s1.sub(s2)
sm=s1.mul(s2)
sd=s1.div(s2)
print(sa)
print(ss)
print(sm)
print(sd)

