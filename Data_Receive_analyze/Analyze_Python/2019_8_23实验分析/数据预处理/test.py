# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 10:11:18 2020

@author: abc47
"""
import numpy as np
#用于除去数据头部不完整帧的数据

data_in=np.load(r"C:\Users\abc47\Desktop\VLP\Data_Receive_analyze\DataStroge\2020_1_13\(60,-20)_0.npy")

for i in range(50):
    if( data_in[i]==0     and data_in[i+9]==1  and 
        data_in[i+18]==2  and data_in[i+27]==3 ):
        data_in=data_in[i:]
        row_num=len(data_in)%9
        find_data=data_in[0:len(data_in)-row_num]
        data_storge=find_data.reshape(int(len(find_data)/9),9)
        break
    
#检查数据中索引是否出错
for x in data_storge[:,0]:
    if(x>7):
        raise Exception("arrange error")

#数据数值计算（数据高八位*256+数据低八位）
calculate_data=np.c_[data_storge[:,0],data_storge[:,1]*256+data_storge[:,2]]
calculate_data=np.c_[calculate_data,data_storge[:,3]*256+data_storge[:,4]]
calculate_data=np.c_[calculate_data,data_storge[:,5]*256+data_storge[:,6]]
calculate_data=np.c_[calculate_data,data_storge[:,7]*256+data_storge[:,8]]  

#----------数据重排-------------------
RowRemainder_Num=calculate_data.shape[0]%8
temp_data=calculate_data[0:-RowRemainder_Num,1:5]
data_out=temp_data.reshape(-1,32)


