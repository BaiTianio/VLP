# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:30:46 2019

@author: abc47
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def normal(mean,x,sigma=2): 
    y=np.exp(-1*((x-mean)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)
    y=y+0.1*y.max()
    y=y/y.max()
    return y
def draw_ideal(xrange,symmetry):#x的范围，对称轴位置
    ideal_data=normal(symmetry,np.arange(xrange))
    plt.plot(ideal_data)

fig=plt.figure()
draw_ideal(64,35)