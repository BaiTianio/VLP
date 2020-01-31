import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd
import numpy as np
import re 
from func_pack import load_data,save_data,data_Process
#1.数据预处理：
#    raw_arrange(data):将原始串行数据整理为n*32的二维数组
class preprocess():
    @staticmethod
    def raw_arrange(data_in):
        for i in range(100):
            if(data_in[i]==0 and data_in[i+9]==1 and data_in[i+27]==3 and data_in[i+36]==4):#判断四个数确保正确
                data_in=data_in[i:]
                print(i)
                break
        row_num=len(data_in)%9
        find_data=data_in[0:len(data_in)-row_num]
        data_storge=find_data.reshape(int(len(find_data)/9),9)
        for x in data_storge[:,0]:
            if(x>7):
                raise Exception("arrange error")
        #数值计算
        calculate_data=np.zeros((data_storge.shape[0],5))   
        calculate_data[:,0]=data_storge[:,0]
        calculate_data[:,1]=data_storge[:,1]*256+data_storge[:,2]
        calculate_data[:,2]=data_storge[:,3]*256+data_storge[:,4]
        calculate_data[:,3]=data_storge[:,5]*256+data_storge[:,6]
        calculate_data[:,4]=data_storge[:,7]*256+data_storge[:,8]
        #保证完整的帧
        calculate_data=calculate_data[0:-int(calculate_data[-1,0])-1,:] 
        #原始数据采集顺序是3214，现需修改为1234排列
        calculate_data[:,[1,2,3,4]]=calculate_data[:,[3,2,1,4]]
        PD32_data=calculate_data[:,1:5].reshape((-1,32))
        return PD32_data

#数据预处理
        

#读取原始数据，对每个PD进行增益归一化，并提取每个PD的值到单个PD数据     
def devide_SiglePD(data,PD_num,times):#从原始数据中提取每个PD在每组数据中的最大值
    pattern=re.compile("data_\d+?_{}".format(times))
    max_value=np.zeros(33)
    i=0
    for index in data.keys():
        if(re.match(pattern,index)):
            max_value[i]=np.max(data[index][:,PD_num])  
            i+=1
    return max_value

if('all_data' not in globals()):
    load_data=load_data()
    all_data=load_data.load_AllData()

PD_max=find_PDMax(all_data)    
saveData=save_data()    
for PD_num in range(32):
    for times in range(1,4):
        PD_data=devide_SiglePD(data=all_data,PD_n num=PD_num+1,times=times)
        PD_data_df=pd.DataFrame(PD_data)/PD_max[PD_num]
        saveData.saveData_csv(PD_data_df,"PD{}_{}".format(PD_num,times))