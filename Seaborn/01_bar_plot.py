'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
Problem statement:
Write a program to draw bar plot of sex against survived for a dataset given in the url
https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv

'''
import seaborn as sns
import pandas as pd
df=pd.read_csv(open("titanic.csv"))
sns.barplot(x="sex",y="survived",data=df)
