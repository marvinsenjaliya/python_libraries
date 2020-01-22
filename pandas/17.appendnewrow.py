"""
Created on:1/22/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
Write a Python program to append a new row 'k' to data frame with given values for each column. Now delete the new row and return the original DataFrame. 
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Values for each column will be:
name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"

"""

import pandas as pd
import numpy as np
exam_data={'name':['Anstasia','Dima','katherine','james','Emily'
,'Michael','Matthew','laura','kevin','jonas'],
'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
'attempts':[1,3,2,3,2,3,1,1,2,1],
'qualify':['yes','no','yes','no','no','yes','yes','no','bo','yes']
}
labels=['a','b','c','d','e','f','g','h','i','j']
df=pd.DataFrame(exam_data,index=labels)
df.loc['k']=[1,'suresh','yes',15.5]
print(df)
df=df.drop('k')
print(df)
