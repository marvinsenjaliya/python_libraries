'''
Created on 23/01/2020
@author: marvin Senjaliya
'''
'''
problem statement:
Write a program to draw a swarm plot of total bill against size  for a  given dataset
        https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
        '''
import seaborn as sns
import pandas as pd

dataFrame=pd.read_csv("tips.csv")
sns.swarmplot(x='total_bill',y='size',data=dataFrame)
