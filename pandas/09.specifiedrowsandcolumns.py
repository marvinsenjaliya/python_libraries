"""
Created on:1/22/2020
@author:Marvin Senjaliya
"""

"""
 Write a Python program to create and display a DataFrame from a s$
        Sample Python dictionary data and list labels:
 
        exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'J$
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 1$
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'n$
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
"""
import numpy as np
import pandas as pd
exam_data={'name':['Anastasia','Dima','katherine','James','Emily'
,'Michael','Matthew','Laura','kevin','jonas'],
'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
'attempts':[1,3,2,3,2,3,1,1,2,1],
'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes'
]}
labels=['a','b','c','d','e','f','g','h','i','j']
df=pd.DataFrame(exam_data,index=labels)
print(df.iloc[[1,2,3],[1,2]])

