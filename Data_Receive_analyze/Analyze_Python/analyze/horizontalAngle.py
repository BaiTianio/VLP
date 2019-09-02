#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:56:55 2019

@author: bxt
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os

def read_data(angle):
    path="/home/bxt/VLP/Data_Receive_analyze/Data/2019_8_23/csv_arranged/"
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

data=read_data(27)[2]

plt.style.use("seaborn-paper")
for PD_num in np.arange(1,data.shape[1]):
    plt.plot(data[:,PD_num],label='PD='+str(PD_num))
plt.legend()    

