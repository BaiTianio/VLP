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


def Load_All():#加载所有数据
    load_path=r"./数据/原始数据"
    data_dict={}    
    FileList=list(filter(lambda x:(x[-4:]==".csv"),os.listdir(load_path)))
    for file in FileList:
        var_name=file[0:-4]
        data_dict[var_name]=np.array(pd.read_csv(load_path+'/'+file))#加载测量数据
    return data_dict

def column_MaxValue(in_data):
        max_num=np.array([])    
        for i in range(in_data.shape[-1]):
            max_num=np.append(max_num,np.max(in_data[:,i]))    
        return max_num

load_data=Load_All()

save_path=r"./数据/每个数据取列最大值/"
for key in load_data.keys():
    max_num=pd.DataFrame(column_MaxValue(load_data[key][:,1:]))
    max_num.to_csv(save_path+"{}.csv".format(key),header=None,index=None)