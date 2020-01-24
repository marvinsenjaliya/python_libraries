'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
problem statement:
Write a program to draw box plot of life expectancy by continent for a data set given in a url 
https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv
'''
import seaborn as sns
import pandas as pd

dataFrame=pd.read_csv("gapminder-FiveYearData.csv")
sns.boxplot(x='lifeExp',y='continent',data=dataFrame)
