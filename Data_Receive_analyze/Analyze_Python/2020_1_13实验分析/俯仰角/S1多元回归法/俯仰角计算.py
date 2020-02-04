# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:48:28 2019

@author: abc47
"""
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import leastsq
import os

#定义拟合函数
def func(x):
    y=np.dot(x,pars.T)
    return y
#拟合参数表
pars=np.array([-0.68171659,  0.29701763, -0.40309471, -0.24367199, -0.00739114,
       -1.09397812, -0.1323149 ,  1.01302055,  0.0677082 ,  0.40330387,
        0.11321053,  0.17602753, -0.17800343,  0.54612606, -0.05793356,
        0.14783358, -0.13706182,  0.16063932, -0.18211319,  0.49671268,
        0.19309777,  0.49001603, -0.08916757,  0.18475841,  0.45557962,
       -0.07905506, -0.31797301,  0.14028483,  0.33901635,  0.11600381,
        0.41476199,  0.12610053])


#数据准备
LoadPath="./数据/"
FileList=list(filter(lambda x:(x[-10:]==",10)_0.npy"),os.listdir(LoadPath)))    
estimateValue_stroge=np.zeros(len(FileList))
realValue_stroge=np.zeros(len(FileList))
cout=0

for file in FileList:
    data_temp=np.load(LoadPath+file)
    estimateValue_stroge[cout]=func(data_temp/data_temp.max())
    if(file[3]==','):
        angle_temp=np.arctan(200/int(file[1:3]))
    else:
        angle_temp=np.arctan(200/int(file[1:4]))
    realValue_stroge[cout]=angle_temp
    cout+=1    

error=(estimateValue_stroge-realValue_stroge)*57.3
   
#load_data=np.load("./数据/(60,-20)_0.npy")
#load_data/=load_data.max()
#ideal_value=np.arctan(200/60)
#estimated_value=func(load_data)
#error=estimated_value-ideal_value
#estiamted_error=estimated_value-ideal_value


##绘图
font = {'family' : 'SimSun',
        'weight' : 'normal',
        'size'   : 15}
plt.rc('font', **font)               # 步骤一（设置字体的更多属性） 
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）  
fig=plt.figure()
plt.plot(error) 
#plt.plot(ideal_value,estiamted_error,label="estiamted error")
#plt.plot(ideal_value,np.zeros(33))
plt.xticks(range(16),np.linspace(50,200,16,endpoint=True))#x轴
plt.xlabel("距离/cm")
plt.ylabel("估计误差/$\degree$")
##plt.legend()


