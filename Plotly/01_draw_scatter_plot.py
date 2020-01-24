'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
problem statement:
Write a program to draw a scatter plot for random 1000 x and y coordinates
'''
import numpy as np
from plotly.offline import iplot
import plotly.graph_objs as go
x=np.linspace(0,1,1000)
y=np.random.rand(1000)

trace= go.Scatter(
    x=x,
    y=y,
    mode='markers'
    )
data=[trace]
figure=go.Figure(data=data)
iplot(figure)
