# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:48:28 2019

@author: abc47
"""
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import leastsq
import os
import re
#定义拟合函数
def func(x):
    y=np.dot(x,pars.T)
    return y
#拟合参数表
pars=np.array([  8.6720305 ,  61.14585577, -34.43250737, -60.45351437,
        -4.42887735, -27.05509737,  24.63921892,  95.9578023 ,
         5.46394687])


#数据准备
LoadPath="./数据/"
FileList=list(filter(lambda x:(x[-6:]=="_0.npy"),os.listdir(LoadPath)))    
estimateValue_stroge=np.zeros(len(FileList))
realValue_stroge=np.zeros(len(FileList))
cout=0

for file in FileList:
    data_temp=np.load(LoadPath+file)
    estimateValue_stroge[cout]=func(data_temp)
    pattern=r",{1}.*\)"
    angle_temp=int(re.search(pattern,file).group()[1:-1])+20
    realValue_stroge[cout]=angle_temp
    cout+=1    
#
error=(estimateValue_stroge-realValue_stroge)
#plt.plot(error)    
#load_data=np.load("./数据/(60,-20)_0.npy")
#load_data/=load_data.max()
#ideal_value=np.arctan(200/60)
#estimated_value=func(load_data)
#error=estimated_value-ideal_value
#estiamted_error=estimated_value-ideal_value


##绘图
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
##plt.legend()


