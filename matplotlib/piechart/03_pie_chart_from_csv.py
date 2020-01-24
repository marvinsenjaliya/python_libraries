'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
problem statement:
 Write a Python programming to create a pie chart of gold medal achievements of five most successful countries in 2016 Summer Olympics. Read the data from a csv file. 
Sample data: 
medal.csv
country,gold_medal
United States,46
Great Britain,27
China,26
Russia,19

'''
from matplotlib import pyplot as plt
import pandas as pd

dataFrame=pd.read_csv("medal.csv")
dataFrame.set_index("country",inplace=True)
plt.title("Gold medal achievements of five most successful countries in 2016 Summer Olympics")
plt.pie(dataFrame["gold_medal"],labels=dataFrame.index,autopct="%1.2f%%")
plt.show()
