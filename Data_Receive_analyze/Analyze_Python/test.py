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


data_in=np.load("../Data/2019_8_23/npy_raw/data_35_2.npy")

def find_frame(data_in):
    for i in range(100):
        if(data_in[i]==0 and data_in[i+9]==1 and data_in[i+27]==3 and data_in[i+45]==5 and
           data_in[i+63]==7):#判断7个数确保正确
            data_out=data_in[i:]
            print(i)
            return data_out
        
find_frame(data_in)  

row_num=len(data_in)%9
find_data=data_in[0:len(data_in)-row_num]
data_storge=find_data.reshape(int(len(find_data)/9),9)

#检验数据帧是否+校正
x_temp=-1;
count=0;
for x in data_storge[:,0]:
    count+=1;
    if(x-x_temp!=1 or x-x_temp!=-7):
        print("error point in %d"%count)   
        
    x_temp=x;
        
     
#数值计算
calculate_data=np.zeros((data_storge.shape[0],5))   
calculate_data[:,0]=data_storge[:,0]
calculate_data[:,1]=data_storge[:,1]*256+data_storge[:,2]
calculate_data[:,2]=data_storge[:,3]*256+data_storge[:,4]
calculate_data[:,3]=data_storge[:,5]*256+data_storge[:,6]
calculate_data[:,4]=data_storge[:,7]*256+data_storge[:,8]
#
##保证完整的帧
#calculate_data=calculate_data[0:-int(calculate_data[-1,0])-1,:] 
##
##原始数据采集顺序是3214，现需修改为1234排列
#calculate_data[:,[1,2,3,4]]=calculate_data[:,[3,2,1,4]]
#PD32_data=calculate_data[:,1:5].reshape((-1,32))

