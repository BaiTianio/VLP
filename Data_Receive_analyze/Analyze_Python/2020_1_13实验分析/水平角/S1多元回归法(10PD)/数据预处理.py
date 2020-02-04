# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:03:20 2019

@author: abc47
"""

import numpy as np
import os
from scipy.optimize import leastsq


def select_data(data_in):
    column_max=data_in.max(axis=0)#按列取最大值
    MaxValue_posi=column_max.argmax()
    ColumnMaxPosi_stroge=(data_in.argmax(axis=0)/data_in.shape[0])
    selected_data=np.zeros(9)
    #---确定中心位置，满足中心在第一列PD的要求-------
    if(MaxValue_posi>27):
        Centre_posi=(int(MaxValue_posi/4+int((MaxValue_posi%4)*2/4))*4)%32
    else:
        Centre_posi=int(MaxValue_posi/4+int((MaxValue_posi%4)*2/4))*4
    #--------------------
    if(Centre_posi==0):
        selected_data[0:4]=ColumnMaxPosi_stroge[28:]
        selected_data[4:9]=ColumnMaxPosi_stroge[0:5]
    elif(Centre_posi==28):
        selected_data[0:8]=ColumnMaxPosi_stroge[24:]
        selected_data[8]=ColumnMaxPosi_stroge[0]
    else:
         selected_data=ColumnMaxPosi_stroge[Centre_posi-4:Centre_posi+5]
    return selected_data
   
LoadPath="../../数据预处理/整理后的数据/无偏移修正的数据/"
FileList=list(filter(lambda x:(x[-6:]=="_0.npy"),os.listdir(LoadPath)))
SavePath="./数据/"
for file in FileList:
    load_data=np.load(LoadPath+file)
    processed_data=select_data(load_data)
    np.save(SavePath+file,processed_data)
