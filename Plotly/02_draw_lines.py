'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
problem statement:
Write a program to draw line a scatter plot for random 100 x and y coordinates
'''
import numpy as np
from plotly.offline import iplot
import plotly.graph_objs as go
x=np.linspace(0,1,100)
y=np.random.rand(100)

trace= go.Scatter(
    x=x,
    y=y,
    mode='lines'
    )
data=[trace]
figure=go.Figure(data=data)
iplot(figure)
