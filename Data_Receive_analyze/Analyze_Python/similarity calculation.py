# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:01:46 2019

@author: abc47
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
import math

def load_AllFile():
    PD_data=np.zeros([33,32])
    load_path="../Data/2019_8_23/npy_singlePD_data/"
    FileList=list(filter(lambda x:(x[-4:]==".npy"),os.listdir(load_path)))
    for file in FileList:
        var_name=file[0:-4]
        locals()[var_name]=np.load(load_path+file)#加载一次测量数据
        locals()[var_name]=locals()[var_name]/locals()[var_name].max()
    for i in range(32):
        var_name="pd"+str(i)+"_1"
        PD_data[:,i]=locals()[var_name]
    return PD_data
PD_data=load_AllFile()

def Eucledian_similarityCalcula(x,y):#相似度判断
    similarity=np.sqrt(np.sum(np.square(x-y)))
    return similarity

def Cos_similarityCalcula(x,y):#相似度判断
    similarity=np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))    
    return similarity


#%%
angle=10
plt.figure()
plt.style.use("seaborn-poster")   
Eu_similarity=np.zeros(33)
for i in range(33):
    Eu_similarity[i]=Eucledian_similarityCalcula(PD_data[angle,:],PD_data[i,:])

plt.plot(Eu_similarity)

#%%
angle=10
plt.figure()
plt.style.use("seaborn-poster")
Cos_similarity=np.zeros(33)
for i in range(33):
    Cos_similarity[i]=Cos_similarityCalcula(PD_data[angle,:],PD_data[i,:])
plt.plot(Cos_similarity)


