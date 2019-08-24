import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

def column_max(in_data):
    max_num=np.int64([])    
    for i in range(in_data.shape[1]):
        max_num=np.append(max_num,np.max(in_data[:,i]))    
    return max_num

def plot_8PD(angle,time):
    data=read_data(angle)[time]
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
angle=62 
sns.set(style="whitegrid")
fig1=plt.figure()    
plot_8PD(angle,1)
fig2=plt.figure()
plot_32PD(angle)