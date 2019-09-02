# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:52:06 2019

@author: abc47
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def my_draw3d(fig,data,**kargs):
    '简化matplotlib 3D的画图'
    Z = data
    x=data.shape[0]
    y=data.shape[1]
    [X,Y]= np.meshgrid(np.arange(x),np.arange(y))#生成坐标网格 
     
     #绘图
    ax3 = fig.add_subplot(1,1,1,projection="3d")
    ax3.plot_surface(X,Y,Z,cmap='rainbow')
     
     #图形优化
       #修改坐标轴
    if(kargs['xticks']):
         plt.xticks(np.linspace(0,x-1,len(kargs['xticks']),dtype=np.int),kargs['xticks'])
    if(kargs['yticks']):
         plt.xticks(np.linspace(0,y-1,len(kargs['yticks']),dtype=np.int),kargs['yticks'])
    if(kargs['xlabel']):      
         plt.xlabel(kargs['xlabel'],fontproperties="SimHei")
    if(kargs['ylabel']):      
         plt.ylabel(kargs['ylabel'],fontproperties="SimHei")
    return 0

def graph_adjust(**kargs):   
     #修改坐标轴
    if('xticks' in kargs):
         plt.xticks(np.linspace(0,kargs['x_scale']-1,len(kargs['xticks']),dtype=np.int),kargs['xticks'])
    if('yticks' in kargs):
         plt.yticks(np.linspace(0,kargs['y_scale']-1,len(kargs['yticks']),dtype=np.int),kargs['yticks'])
         
    if('ticks_size' in kargs):
         plt.xticks(fontsize=kargs['ticks_size'])    
         plt.yticks(fontsize=kargs['ticks_size'])    
         
    if('xlabel' in kargs):      
         plt.xlabel(kargs['xlabel'],fontsize=kargs['label_size'])
    if('ylabel' in kargs):      
         plt.ylabel(kargs['ylabel'],fontsize=kargs['label_size'])
    return 0

def font_config():
    font = {'family' : 'SimHei',
            'weight' : 'normal',
            'size'   : '10'}
    plt.rc('font', **font)               # 步骤一（设置字体的更多属性）
    plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）  
    return 0

#plt.style.use("seaborn-paper") 
#fig=plt.figure(figsize=(4,4),dpi=300)

#data=np.ones([10,10])
#fig1=draw_3d(data,xticks=['j','k','l'])
