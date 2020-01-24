''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
problem statement:
Write a program to draw a box plot of day by tips for a dataset given in a url
 https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
'''
import seaborn as sns
import pandas as pd

dataFrame=pd.read_csv("tips.csv")
sns.boxplot(x='day',y='tip',data=dataFrame)
