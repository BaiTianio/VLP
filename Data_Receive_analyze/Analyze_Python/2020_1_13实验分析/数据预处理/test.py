# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:25:48 2019
@author: BaiTianio
"""

import numpy as np
import os
##########数据整理函数，带有数据偏移功能################    
#输入为原始串行数据，输出为排列好的32列数据
def DataArrange_Setoff(data_in):  
    #用于除去数据头部不完整帧的数据
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

    #=========将数据进行分组偏移==========
    #------------将数据重新分组--------
    def data_divide_group(data_in,group_num):  
        row_num=int(data_in.shape[0]/8)
        PDarray_data=np.zeros((row_num,8))
        for i in range(row_num):  
            if(data_in[i*8,0]==0 and data_in[i*8+7,0]==7):
                PDarray_data[i,:]=data_in[i*8:(i+1)*8,group_num].T        
        PDarrayGroup_data=np.c_[PDarray_data[:,0],PDarray_data[:,1],PDarray_data[:,2],PDarray_data[:,3],
                                PDarray_data[:,4],PDarray_data[:,5],PDarray_data[:,6],PDarray_data[:,7]]
        return PDarrayGroup_data
    PDarrayA_DataGroup=data_divide_group(calculate_data,3)#
    PDarrayB_DataGroup=data_divide_group(calculate_data,2)#
    PDarrayC_DataGroup=data_divide_group(calculate_data,1)#
    PDarrayD_DataGroup=data_divide_group(calculate_data,4)#
    #-------------------------------------
    #-------------数据偏移----------------
    PDarrayB_DataGroup=np.roll(PDarrayB_DataGroup,int(PDarrayB_DataGroup.shape[0]*3/4),axis=0)#
    PDarrayC_DataGroup=np.roll(PDarrayC_DataGroup,int(PDarrayC_DataGroup.shape[0]*2/4),axis=0)#
    PDarrayD_DataGroup=np.roll(PDarrayD_DataGroup,int(PDarrayD_DataGroup.shape[0]*1/4),axis=0)#
    #------------------------------------
    #----------数据重排-------------------
    row_num=np.max([PDarrayA_DataGroup.shape[0],PDarrayB_DataGroup.shape[0],
                PDarrayC_DataGroup.shape[0],PDarrayD_DataGroup.shape[0]])
    data_summary=np.zeros((row_num,32))
    for i in range(8):
        data_summary[:,i*4]=PDarrayA_DataGroup[:,i]
        data_summary[:,i*4+1]=PDarrayB_DataGroup[:,i]
        data_summary[:,i*4+2]=PDarrayC_DataGroup[:,i]
        data_summary[:,i*4+3]=PDarrayD_DataGroup[:,i]
    #--------------------------------------
    return data_summary    
    
##########数据整理函数，不进行数据偏移################    
#输入为原始串行数据，输出为排列好的32列数据
def DataArrange_WithoutSetoff(data_in):  
    #用于除去数据头部不完整帧的数据
    for i in range(100):
        if( data_in[i]==0     and data_in[i+9]==1  and 
            data_in[i+18]==2  and data_in[i+27]==3 and
            data_in[i+36]==4  and data_in[i+45]==5):
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
    if(RowRemainder_Num==0):
        temp_data=calculate_data[:,1:5]
    else:
        temp_data=calculate_data[0:-RowRemainder_Num,1:5]
    data_out=temp_data.reshape(-1,32)
    return data_out    

#######调用########

LoadPath="../../../DataStroge/2020_1_13/" 
FileList=list(filter(lambda x:(x[-4:]==".npy"),os.listdir(LoadPath)))
SavePath="./整理后的数据/无偏移修正的数据/"
file="(110,40)_0.npy"
RawData=np.load(LoadPath+file)
ArrangedData=DataArrange_WithoutSetoff(RawData)
#np.save(SavePath+file,ArrangedData)

#file="(80,40)_2.npy"
#RawData=np.load(LoadPath+file)
#ArrangedData=DataArrange_WithoutSetoff(RawData)
#np.save(SavePath+file,ArrangedData)

