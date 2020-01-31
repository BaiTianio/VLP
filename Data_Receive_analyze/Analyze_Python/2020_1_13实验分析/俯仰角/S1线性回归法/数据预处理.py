# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:03:20 2019

@author: abc47
"""

import numpy as np
import os
import matplotlib.pyplot as plt 
import pandas as pd
from scipy.optimize import leastsq

def column_MaxValue(in_data):
        max_num=np.array([])    
        for i in range(in_data.shape[-1]):
            max_num=np.append(max_num,np.max(in_data[:,i]))    
        return max_num

   
LoadPath="../../数据预处理/整理后的数据/无偏移修正的数据/"
FileList=list(filter(lambda x:(x[-6:]=="_0.npy"),os.listdir(LoadPath)))
SavePath="./数据/"
for file in FileList:
    load_data=np.load(LoadPath+file)
    processed_data=column_MaxValue(load_data)
    np.save(SavePath+file,processed_data)

