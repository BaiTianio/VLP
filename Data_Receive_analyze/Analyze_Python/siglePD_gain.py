import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
import math

def load_AllFile():
    PD_data=np.zeros([33,32])
    load_path="../Data/2019_8_23/npy_singlePD_data/"
    FileList=list(filter(lambda x:(x[-4:]==".npy"),os.listdir(load_path)))
    for file in FileList:
        var_name=file[0:-4]
        locals()[var_name]=np.load(load_path+file)#加载一次测量数据
        locals()[var_name]=locals()[var_name]/locals()[var_name].max()
    for i in range(32):
        var_name="pd"+str(i)+"_1"
        PD_data[:,i]=locals()[var_name]
    return PD_data
PD_data=load_AllFile()

def out_maxposi():
    for i in range(32):
        var_name="pd"+str(i)+"_1"
        max_pos=globals()[var_name].argmax()
        print(i,max_pos)
    return 0

def PD_dataCollc():
    PD_data=np.zeros([33,32])
    for i in range(32):
        var_name="pd"+str(i)+"_1"
        PD_data[:,i]=globals()[var_name]
#%%

LED_angle=22
x=np.arange(32)
plt.style.use("seaborn-poster")    

fig1=plt.figure()
plt.plot(x,PD_data[LED_angle,:])
plt.xticks(x,fontsize=10)
plt.grid(axis='x',linestyle='-.') 

#%%
PD_num=15
x=np.arange(33)
plt.style.use("seaborn-poster")    

fig1=plt.figure()
plt.plot(x,PD_data[:,PD_num])
plt.xticks(x,fontsize=10)
plt.grid(axis='x',linestyle='-.') 


   
#
# 
#fig2=plt.figure()
#plt.plot(x,PD_data[angle,:])
#plt.xticks(x,fontsize=10)
#plt.grid(axis='x',linestyle='-.')



