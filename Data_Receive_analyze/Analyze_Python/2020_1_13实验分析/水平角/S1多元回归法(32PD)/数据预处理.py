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
    ColumnMax_posi=data_in.argmax(axis=0)
    ColumnMax_posi=ColumnMax_posi/data_in.shape[0]-0.5
    if(MaxValue_posi<3):
        ColumnMax_posi[MaxValue_posi+4:-(3-MaxValue_posi)]=0
    elif(MaxValue_posi>28):
        ColumnMax_posi[(3-(31-MaxValue_posi)):(MaxValue_posi-3)]=0
    else:
        ColumnMax_posi[0:MaxValue_posi-3]=0
        ColumnMax_posi[MaxValue_posi+4:]=0
    return ColumnMax_posi
   
LoadPath="../../数据预处理/整理后的数据/无偏移修正的数据/"
FileList=list(filter(lambda x:(x[-6:]=="_0.npy"),os.listdir(LoadPath)))
SavePath="./数据/"
for file in FileList:
    load_data=np.load(LoadPath+file)
    processed_data=select_data(load_data)
    np.save(SavePath+file,processed_data)

