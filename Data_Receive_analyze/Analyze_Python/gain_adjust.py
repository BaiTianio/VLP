import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import re
import os

def load_AllFile():
    load_path="../Data/2019_8_23/npy_arranged/"
    FileList=list(filter(lambda x:(x[-4:]==".npy"),os.listdir(load_path)))
    for file in FileList:
        var_name=file[0:-4]
        exec(var_name+'=np.load(load_path+file)',locals(),globals())
    return 0
load_AllFile()

def column_max(in_data):
    max_num=np.int64([])    
    for i in range(in_data.shape[1]):
        max_num=np.append(max_num,np.max(in_data[:,i]))    
    return max_num

def plot_8PD(angle,time):
    exec("data=data_{}_{}".format(angle,time),globals())
    index=np.arange(8)*4
    for i in range(4):
        max_num=column_max(data[:,index+i])
        plt.plot(max_num,label='PDarray='+str(i))
    plt.title("angle={}".format(angle))  
    plt.legend()
#        plt.ylim(100,180)
def plot_32PD(angle):
    data=read_data(angle)
    for i in range(3):
        plt.plot(column_max(data[i]),label='times='+str(i))  
    plt.title("angle={}".format(angle))    
    plt.legend()
 

#%%
plt.style.use("seaborn-poster")    
angle=65 

fig1=plt.figure()    
plot_8PD(angle,1)
#fig2=plt.figure()
#plot_32PD(angle)