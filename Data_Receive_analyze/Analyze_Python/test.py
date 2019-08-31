# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:00:18 2019

@author: abc47
"""
import plotly.graph_objects as go
fig = go.FigureWidget(data=go.Bar(y=[2, 3, 1]))
fig.write_image('figure.png')