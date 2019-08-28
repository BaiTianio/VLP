# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:00:18 2019

@author: abc47
"""
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import math

def normal_distribution(mean,x = np.arange(33),sigma=2): 
    y=np.exp(-1*((x-mean)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)
    y=y+0.1*y.max()
    y=y/y.max()
    return y

x = np.arange(33)
mean, sigma = 21, 2
y=normal_distribution(mean=21)
fig=plt.figure()
plt.plot(x,y, 'r', label='m=0,sig=1')
plt.xticks(x,fontsize=5)
plt.legend()
plt.grid()