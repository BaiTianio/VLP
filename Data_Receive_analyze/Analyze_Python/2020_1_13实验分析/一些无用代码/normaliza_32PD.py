import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import re
import os
import tkinter as tk
from tkinter import filedialog



        
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
