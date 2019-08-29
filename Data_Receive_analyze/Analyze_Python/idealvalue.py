# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:30:46 2019

@author: abc47
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def normal(mean,x = np.arange(33),sigma=2): 
    y=np.exp(-1*((x-mean)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)
    y=y+0.1*y.max()
    y=y/y.max()
    return y

ideal_data=np.zeros([33,32])
for i in range(32):
    ideal_data[:,i]=normal(mean=i)

oneangel=ideal_data[10,:]
plt.plot(oneangel)
