import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import re
import os
import tkinter as tk
from tkinter import filedialog


#%%

load_AllFile('.npy')
#%%


def load_AllFile():
    PD_data=np.zeros([3,33,32])
    load_path=r"../../Data/2019_8_23/npy_singlePD_data/"
    FileList=list(filter(lambda x:(x[-4:]==".npy"),os.listdir(load_path)))
    for file in FileList:
        var_name=file[0:-4]
        locals()[var_name]=np.load(load_path+file)#加载一次测量数据
        locals()[var_name]=locals()[var_name]/locals()[var_name].max()
    for times in range(3):#三次采集数据全部取出
        for PD_num in range(32):
            var_name="pd{}_{}".format(PD_num,times+1)
            PD_data[times,:,PD_num]=locals()[var_name]
    return PD_data
PD_data=load_AllFile()

        
def column_max(in_data):
    max_num=np.int64([])    
    for i in range(len(in_data)):
        max_num=np.append(max_num,np.max(in_data))    
    return max_num


def plot_32PD(angle):#通过signlePD数据来画图
    global data,test_num
    test_num=int((angle-15)/2)
    for times in range(3):
        data=PD_data[times,test_num,:]
        plt.plot(data,label='times='+str(times))  
        plt.title("angle={}".format(angle))    
        plt.legend()
    return 0

def normal(mean,x = np.arange(33),sigma=2):#高斯函数 
    y=np.exp(-1*((x-mean)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)
    y=y+0.1*y.max()
    y=y/y.max()
    return y


#%%
fig=plt.figure()
plt.style.use("seaborn-paper") 
font = {'family' : 'SimHei',
        'weight' : 'bold',
        'size'   : '16'}
plt.rc('font', **font)               # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）   

angle=47
plt.xlabel("PD 序号")
plt.ylabel("光照度(lux)") 
plt.xlim(0,32)
plt.ylim(0,1)  
plt.title("归一化后的数据")
plot_32PD(angle)
