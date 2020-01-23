"""
Created on:1/23/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to create multiple types of charts
"""
import pandas as pd
import matplotlib.pyplot as plt
data=[['m',34,123],['f',40,114],['f',37,135],['m',44,183]]
df=pd.DataFrame(data,columns=['gender','age','sales'])
df.hist()
plt.show()
df.plot.box()
plt.boxplot(df['age'])
plt.show()
