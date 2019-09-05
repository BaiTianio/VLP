# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:48:28 2019

@author: abc47
"""
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt 
from scipy.stats import norm
#%%步骤一
def find_PDMax(all_data):
    PD_max=np.zeros(32)
    PD_data=np.array([])
    i=0
    for PD_num in range(32):
        for index in all_data.keys():
            PD_data=np.append(PD_data,np.max(all_data[index][:,PD_num+1]))  
            
        PD_max[i]=np.max(PD_data)
        PD_data=np.array([])
        i+=1
    return PD_max
load_path="./数据"
load_data={}    
FileList=os.listdir(load_path)
for file in FileList:
    var_name=file[0:-4]
    load_data[var_name]=np.array(pd.read_csv(load_path+'/'+file))#加载测量数据

PD_max=find_PDMax(load_data)#获取每个PD最大增益
for index in load_data.keys():
    for PD_num in range(32):
        load_data[index][:,PD_num+1]/=PD_max[PD_num]#进行增益调整
#%%步骤二
def column_MaxValue(in_data):
    max_num=np.array([])    
    for i in range(in_data.shape[-1]):
        max_num=np.append(max_num,np.max(in_data[:,i]))    
    return max_num

def draw_all_PD(data1,data2,data3):
    for PD_num in np.arange(32):
        x=np.arange(15,80,2)
        ideal_value=norm.pdf(np.arange(0,90,0.1), loc=7.5+PD_num*2.5, scale=5) #正态分布 
        plt.style.use("seaborn-poster")    
        fig1=plt.figure()
        plt.title("PD="+str(PD_num))
        plt.plot(x,data1[:,PD_num],label='Times=1')
        plt.plot(x,data2[:,PD_num],label='Times=2')
        plt.plot(x,data3[:,PD_num],label='Times=3')
        plt.plot(np.arange(0,90,0.1),ideal_value/ideal_value.max(),label='ideal value')
        
        plt.xlim((15,80))
        plt.ylim((0,1))
        plt.legend()
        plt.xticks(np.arange(14,80,1),fontsize=6)
        plt.grid(axis='x',linestyle='-.')
        plt.savefig("./Picture/PD"+str(PD_num)+".jpg")
        plt.close()     
all_PDmax_1=np.zeros((33,32))
all_PDmax_2=np.zeros((33,32))
all_PDmax_3=np.zeros((33,32))
i=0
for angle in range(15,80,2):
    all_PDmax_1[i]=column_MaxValue(load_data['data_{}_1'.format(angle)][:,1:])
    all_PDmax_2[i]=column_MaxValue(load_data['data_{}_2'.format(angle)][:,1:])
    all_PDmax_3[i]=column_MaxValue(load_data['data_{}_3'.format(angle)][:,1:])
    i+=1
draw_all_PD(all_PDmax_1,all_PDmax_2,all_PDmax_3)#画数据   
#%%步骤三
