# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:30:46 2019

@author: abc47
"""
import numpy as np
import matplotlib.pyplot as plt
import math
import my_draw 
from scipy.stats import norm

value=norm.pdf(np.arange(32), loc=24, scale=2) #正态分布 

my_draw.graph_adjust(xticks=[r'0$\degree$',r'10$\degree$',r'20$\degree$',
                             r'30$\degree$',r'40$\degree$',r'50$\degree$',
                             r'60$\degree$',r'70$\degree$',r'80$\degree$',r'90$\degree$'],x_scale=90) 

plt.xlabel(r"角度$\beta$($\degree$)")
plt.ylabel("归一化光照度")
#plt.title('俯仰角理想分布曲线')

ideal_data=normal(90,45)
plt.plot(ideal_data,label='真实值')

ideal_data=normal(90,55)
plt.plot(ideal_data,label='测量值')
plt.legend()




