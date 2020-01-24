'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
Problem statement:
Write a program to draw a scatter plot for a given dataset and show datalabels on hover
https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv
'''
import plotly.express as ply
import pandas as pd

dataFrame=pd.read_csv("2014_usa_states.csv")
figure=ply.scatter(dataFrame, x='Population',y='Rank',color='State',hover_data=['Postal'])
figure.show()
