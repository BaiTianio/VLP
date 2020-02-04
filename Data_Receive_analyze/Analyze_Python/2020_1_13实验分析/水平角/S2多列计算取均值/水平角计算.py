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
    y=np.dot(x*x,pars.T)
    return y
#拟合参数表
pars=np.array([ 1.00000000e+00,  1.00000000e+00,  1.00000000e+00,  1.00000000e+00,
        1.00000000e+00,  1.00000000e+00,  1.00000000e+00,  1.00000000e+00,
        1.00000000e+00,  1.00000000e+00,  7.44952944e+04, -3.18716713e+04,
       -5.93409591e+01,  3.39270053e+02, -1.16910199e+03, -1.33418119e+01,
       -8.05274649e+00,  1.66959825e+02,  6.68955390e+02, -1.97622518e+02,
        2.39194873e+01,  1.50635298e+02,  2.79258041e+02, -3.17710392e+02,
        9.95198466e+01,  2.43023462e+02,  5.18720435e+02, -2.39059383e+02,
        9.88349564e+01, -5.15166330e+01,  1.35236395e+03, -2.78409217e+01])


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


