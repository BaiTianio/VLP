import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os

def gain_adjust(in_data):
    in_data[:,16]=in_data[:,16]*1.5#A0P4
    in_data[:,17]=in_data[:,17]*0.5#A1P4
    in_data[:,18]=in_data[:,18]*5.5#A2P4
    in_data[:,19]=in_data[:,19]*1.5#A3P4
       
    in_data[:,20]=in_data[:,20]*0.8#A0P5
    in_data[:,21]=in_data[:,21]*0.95#A1P5
    in_data[:,22]=in_data[:,22]*1#A2P5
    in_data[:,23]=in_data[:,23]*0.874#A3P5
    
    in_data[:,24]=in_data[:,24]*0.769#A0P6
    in_data[:,25]=in_data[:,25]*1#A1P6
    in_data[:,26]=in_data[:,26]*0.366#A2P6
    in_data[:,27]=in_data[:,27]*0.44#A3P6
    return in_data
def read_data(angle):
    path="/home/bxt/VLP/VLP_DataProcess/Data/data_csv/"
    file_list=os.listdir(path)
    csv_list=list(filter(lambda x:(x[-4:]==".csv" and x[5:7]==str(angle)),file_list))
    data=[0,0,0]
    for i in range(len(csv_list)):
        data[i]=np.array(pd.read_csv(path+csv_list[i]))  
        data[i]=gain_adjust(data[i])
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
    plt.legend()
#        plt.ylim(100,180)
def plot_32PD(angle):
    data=read_data(angle)
    for i in range(3):
        plt.plot(column_max(data[i]),label='times='+str(i))  
    plt.legend()
sns.set(style="whitegrid")
fig1=plt.figure()    
plot_8PD(64,2)
fig2=plt.figure()
plot_32PD(64)