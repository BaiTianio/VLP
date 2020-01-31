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
    for index_num in range(23):#只处理35°到79°的数据，共23组数据
        index='data_'+str(index_num*2+35)+'_1.csv'
        read_data=np.array(pd.read_csv(load_path+index))
        maxPos=column_maxposi(read_data[:,1:]).T#获得每列的最大位置
        maxPos_percent=maxPos/read_data.shape[0]#每列最大位置归一化
        all_maxPos[index_num]=maxPos_percent
    return all_maxPos

load_data=Load_All()        

modefid_maxPosi=np.zeros((23,5))
for index_num in range(23):#只处理35°到79°的数据，共23组数据
    PDnum=int(((index_num*2+35)-7.5)/2.5)
    select_PD=[PDnum-2,PDnum-1,PDnum,PDnum+1,PDnum+2]
    select_maxPosi=load_data[index_num,select_PD]
    #按照PD阵列位置修正
    PD_posi=np.array([(PDnum-2)%4,(PDnum-1)%4,(PDnum)%4,(PDnum+1)%4,(PDnum+2)%4])
    modefid_maxPosi[index_num]=(select_maxPosi+PD_posi*0.25)%1
error_dist=((modefid_maxPosi.mean(axis=1)-0.5)*360)%2





#绘图
font = {'family' : 'SimSun',
        'weight' : 'normal',
        'size'   : 15}
plt.rc('font', **font)               # 步骤一（设置字体的更多属性） 
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）  
fig=plt.figure()

x=np.arange(35,80,2)
plt.plot(x,error_dist,label="estiamted error")
plt.xlabel("角度/$\degree$")
plt.ylabel("估计误差/$\degree$")
#plt.legend()


