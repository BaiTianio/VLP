#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:24:26 2019

@author: bxt
"""

from scipy import poly1d
import numpy as np
import matplotlib.pyplot as plt

ang=np.append(np.arange(40,0,-2.5),np.arange(0,40,2.5))
radian=ang/180*np.pi
a=np.sin(radian)
b=np.cos(radian)
y=b-2*a
y[y<0]=0
plt.plot(y)

