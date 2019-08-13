#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:24:26 2019

@author: bxt
"""

from scipy import poly1d
import numpy as np
import matplotlib.pyplot as plt

p=poly1d([-1,-200,1000])
x=np.arange(0,31)
plt.plot(x,p(x))

