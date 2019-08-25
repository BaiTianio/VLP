# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 20:19:39 2019

@author: abc47
"""
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os

def load_AllFile():
    load_path="../Data/2019_8_23/npy_arranged/"
    FileList=list(filter(lambda x:(x[-4:]==".npy"),os.listdir(load_path)))
    for file in FileList:
        var_name=file[0:-4]
        exec(var_name+'=np.load(load_path+file)',locals(),globals())
    return 0
load_AllFile()

def find_siglePDmax_allData(pd_num,time):
    max_num=np.int64([])
    pattern=re.compile("data_\d+?_{}".format(time))
    loca_var=list(globals())
    for data in loca_var:
        if(re.match(pattern,data)):
            print(data)
            max_num=np.append(max_num,np.max(globals()[data][:,pd_num]))           
    return max_num
#%%
PD_num=25
PD_data_1=find_siglePDmax_allData(PD_num,1)
PD_data_2=find_siglePDmax_allData(PD_num,2)
PD_data_3=find_siglePDmax_allData(PD_num,3)

plt.style.use("seaborn-poster")    
fig1=plt.figure() 
plt.plot(np.arange(15,79,2),PD_data_1)
plt.plot(np.arange(15,79,2),PD_data_2)
plt.plot(np.arange(15,79,2),PD_data_3)
plt.xlim((10,80))

