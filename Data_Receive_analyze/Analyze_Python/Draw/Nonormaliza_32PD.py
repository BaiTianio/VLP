import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import re
import os

def load_AllFile():
    PD_data=np.zeros([33,32])
    load_path=r"../../Data/2019_8_23/npy_arranged/"
    FileList=list(filter(lambda x:(x[-4:]==".npy"),os.listdir(load_path)))
    for file in FileList:
        var_name=file[0:-4]
        globals()[var_name]=np.load(load_path+file)#加载一次测量数据
    return 0
PD_data=load_AllFile()

def column_max(in_data):
    max_num=np.int64([])    
    for i in range(in_data.shape[1]):
        max_num=np.append(max_num,np.max(in_data[:,i]))    
    return max_num


def plot_32PD(angle):#通过arrange数据来画图
    for i in range(1,4):
        vari_name='data_{}_{}'.format(angle,i)
        data=globals()[vari_name]
        plt.plot(column_max(data),label='times='+str(i))  
    plt.title("angle={}".format(angle))    
    plt.legend()

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
angle=45

plt.xlabel("PD 序号")
plt.ylabel("光照度(lux)") 
ideal_data=np.zeros([33,33])
plt.title("没有归一化的数据")  
plot_32PD(angle)
