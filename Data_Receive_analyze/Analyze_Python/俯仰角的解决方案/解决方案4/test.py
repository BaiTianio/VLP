# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:03:20 2019

@author: abc47
"""

import numpy as np
import os
import matplotlib.pyplot as plt 
import myDP
from scipy.optimize import leastsq

#load_data=myDP.Load_Save.Load_files(initialdir=os.getcwd()+'/')

# data provided
#x = np.array([[1, 50, 5, 200], [1, 50, 5, 400], [1, 50, 5, 600], [1, 50, 5, 800], [1, 50, 5, 1000],
#             [1, 50, 10, 200], [1, 50, 10, 400], [1, 50, 10, 600], [1, 50, 10, 800], [1, 50, 10, 1000],
#             [1, 60, 5, 200], [1, 60, 5, 400], [1, 60, 5, 600], [1, 60, 5, 800], [1, 60, 5, 1000],
#             [1, 60, 10, 200], [1, 60, 10, 400], [1, 60, 10, 600], [1, 60, 10, 800], [1, 60, 10, 1000],
#             [1, 70, 5, 200], [1, 70, 5, 400], [1, 70, 5, 600], [1, 70, 5, 800], [1, 70, 5, 1000],
#             [1, 70, 10, 200], [1, 70, 10, 400]])
x=[[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
y=[2,4,6,8]
#y = np.array([int(x[0:2]) for x in load_data.keys()]) 
funcLine=lambda tpl,x: np.dot(x, tpl)
func = funcLine
ErrorFunc = lambda tpl, x, y: func(tpl, x)-y
tplInitial=[1.0, 1.0, 1.0, 1.0]
tplFinal, success = leastsq(ErrorFunc, tplInitial, args=(x, y))
#print('linear fit', tplFinal)

