'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
problem statement:
Write a program to draw a violin plot of “species” against “sepal length” for a dataset given in a url 
 	https://github.com/mwaskom/seaborn-data/blob/master/iris.csv
'''
import seaborn as sns
import pandas as pd

dataFrame=pd.read_csv("iris.csv")
sns.violinplot(x='species',y='sepal_length',data=dataFrame)
