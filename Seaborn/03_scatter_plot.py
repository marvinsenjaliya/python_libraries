'''
Created on 23/01/2020
@author: marvin Senjaliya
'''
'''
problem statement:
Write a program to draw a scatter plot of “day” against “total bill” for a dataset given in a url 
 https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
'''
import seaborn as sns
import pandas as pd

dataFrame=pd.read_csv("tips.csv")
sns.scatterplot(x='day',y='total_bill',data=dataFrame)
