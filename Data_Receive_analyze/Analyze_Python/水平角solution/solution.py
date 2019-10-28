# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:48:28 2019

@author: abc47
"""
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import leastsq
import pandas as pd
import os


#找到数据每一列的最大位置
def column_maxposi(in_data):
    max_loc=np.int64([])    
    for i in range(in_data.shape[1]):
        max_loc=np.append(max_loc,np.argmax(in_data[:,i]))    
    return max_loc

#数据准备
def Load_All():#加载所有数据
    load_path=r"./整理后的数据/"
    all_maxPos=np.zeros((23,32))    
    for index_num in range(10,33):#只处理35°到79°的数据
        index='data_'+str(index_num*2+15)+'_1.csv'
        read_data=np.array(pd.read_csv(load_path+index))
        maxPos=column_maxposi(read_data[:,1:]).T#获得每列的最大位置
        maxPos_percent=maxPos/read_data.shape[0]#每列最大位置归一化
        all_maxPos[index_num-10]=maxPos_percent
    return all_maxPos


X=Load_All()        



#绘图
#font = {'family' : 'SimSun',
#        'weight' : 'normal',
#        'size'   : 15}
#plt.rc('font', **font)               # 步骤一（设置字体的更多属性） 
#plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）  
#fig=plt.figure()
#plt.plot(ideal_value,estiamted_error,label="estiamted error")
#plt.plot(ideal_value,np.zeros(33))
#plt.xlabel("角度/$\degree$")
#plt.ylabel("估计误差/$\degree$")
#plt.legend()


