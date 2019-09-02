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

ideal_data=np.zeros([33,33])
for i in range(33):
    ideal_data[:,i]=normal(mean=i)

oneangel=ideal_data[10,:]


plt.style.use('seaborn-paper')

font = {'family' : 'SimHei',
        'weight' : 'bold',
        'size'   : '16'}
plt.rc('font', **font)               # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）

plt.xlabel("PD 序号")
plt.ylabel("光照度(lux)")
plt.title('俯仰角理想分布曲线')
plt.plot(oneangel)
