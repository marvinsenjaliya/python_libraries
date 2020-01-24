'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
Problem statement:
Write a program to draw a point plot for sex against survived for a dataset given in url
https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv

'''
import pandas as pd
import seaborn as sns

dataFrame=pd.read_csv("titanic.csv")
sns.pointplot(x='sex',y='survived',data=dataFrame)
