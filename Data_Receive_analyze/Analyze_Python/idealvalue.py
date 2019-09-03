# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:30:46 2019

@author: abc47
"""
import numpy as np
import matplotlib.pyplot as plt
import math
import my_draw 
def normal(xrange,mean,sigma=3): 
    x=np.arange(xrange)
    y=np.exp(-1*((x-mean)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)
    y=y+0.1*y.max()
    y=y/y.max()
    return y
#def draw_ideal(xrange,symmetry):#x的范围，对称轴位置
#    ideal_data=normal(symmetry,np.arange(xrange))
#    plt.plot(ideal_data)

fig=plt.figure()
#my_draw.font_config(size=26)
#font = {'family' : 'SimHei',
#        'weight' : 'normal',
#        'size'   : '6'}
#plt.rc('font', **font)               # 步骤一（设置字体的更多属性）
#plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）  
    
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




