import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os

def read_data(angle):
    path="../Data/data_csv/"
    file_list=os.listdir(path)
    csv_list=list(filter(lambda x:(x[-4:]==".csv" and x[5:7]==str(angle)),file_list))
    data=[0,0,0]
    for i in range(len(csv_list)):
        data[i]=np.array(pd.read_csv(path+csv_list[i]))  
    return data

def column_maxposi(in_data):
    max_loc=np.int64([])    
    for i in range(in_data.shape[1]):
        max_loc=np.append(max_loc,np.argmax(in_data[:,i]))    
    return max_loc

def plot_32maxposi(angle):
    data=read_data(angle)
    for i in range(3):
        max_loc=column_maxposi(data[i])
        plt.plot(max_loc,label='time='+str(i))
        plt.title(("Angle={}".format(angle)))
        plt.legend()
        plt.xlim(0,31)
#        plt.ylim(100,180)
        
def plot_8maxposi(angle,time):
    data=read_data(angle)[time]
    index=np.arange(8)*4
    for i in range(4):
        max_loc=column_maxposi(data[:,index+i])
        plt.plot(max_loc,label='PDarray='+str(i))
        plt.title(("times={}".format(time)))
        plt.legend()
        plt.ylim(50,200)
        
def plot_1PDmaxPosi(PD_num):
    max_loc=np.int64([]) 
    for i in list(range(30,46))+list(range(46,80,2)):
        data=read_data(i)
        for j in range(3):
            max_loc=np.append(max_loc,np.argmax(data[j][:,PD_num]))
    print("PD%d=%f"%(PD_num,max_loc[40:90].mean()))
    plt.plot(max_loc,label="PD="+str(PD_num))
    plt.xlim(40,90)
    plt.ylim(100,180)
    plt.legend()
#%%
plot_1PDmaxPosi(21)
plot_1PDmaxPosi(22) 
plot_1PDmaxPosi(23)
plot_1PDmaxPosi(24)
plot_1PDmaxPosi(25)  
    
#%% 
angle=68
fig=plt.figure()
plt.suptitle(("Angle={}".format(angle)))
plt.subplot(131)
plot_8maxposi(angle,0)
plt.subplot(132)
plot_8maxposi(angle,1)
plt.subplot(133)
plot_8maxposi(angle,2)
#%%
fig=plt.figure()
plt.subplot(121)
plot_32maxposi(60)
plt.subplot(122)
plot_32maxposi(62)
