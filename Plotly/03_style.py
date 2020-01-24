'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
problem statement:
Write a program to draw a scatter plot for random 500 x and y coordinates and style it
'''
from plotly.offline import iplot
import plotly.graph_objs as go
import numpy as np

x=np.linspace(0,1,500)
y=np.random.rand(500)

trace= go.Scatter(
    x=x,
    y=y,
    mode="markers",
    marker=dict(
    color="LightBlue",
    size=15,
        opacity=0.9,
        line=dict(
        color="MediumBlue",
        width=2)
    )
)
data=[trace]
figure=go.Figure(data=data)
iplot(figure)
