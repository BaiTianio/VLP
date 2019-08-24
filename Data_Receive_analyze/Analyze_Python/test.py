#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:24:26 2019

@author: bxt
"""

from scipy import poly1d
import numpy as np
import matplotlib.pyplot as plt
import os

data_in=np.load("../Data/2019_8_23/npy_raw/data_35_0.npy")
for i in range(100):
    if(data_in[i]==0 and data_in[i+9]==1 and data_in[i+18]==2):
        data_in=data_in[i:]
        print(i)
        break
row_num=len(data_in)%9
find_data=data_in[0:len(data_in)-row_num]
data_storge=find_data.reshape(int(len(find_data)/9),9)
for x in data_storge[:,0]:
    if(x>7):
        raise Exception("arrange error")
     
#数值计算
calculate_data=np.zeros((data_storge.shape[0],5))   
calculate_data[:,0]=data_storge[:,0]
calculate_data[:,1]=data_storge[:,1]*256+data_storge[:,2]
calculate_data[:,2]=data_storge[:,3]*256+data_storge[:,4]
calculate_data[:,3]=data_storge[:,5]*256+data_storge[:,6]
calculate_data[:,4]=data_storge[:,7]*256+data_storge[:,8]

#保证完整的帧
calculate_data=calculate_data[0:-int(calculate_data[-1,0])-1,:] 

#原始数据采集顺序是3214，现需修改为1234排列
calculate_data[:,[1,2,3,4]]=calculate_data[:,[3,2,1,4]]
PD32_data=calculate_data[:,1:5].reshape((-1,32))

