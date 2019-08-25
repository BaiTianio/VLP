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
        globals()[var_name]=np.load(load_path+file)
    return 0
load_AllFile()

def find_siglePDmax_allData(PD_num,time):
    max_num=np.zeros(33)
    pattern=re.compile("data_\d+?_{}".format(time))
    loca_var=list(globals())
    i=0
    for data in loca_var:
        if(re.match(pattern,data)):
            max_value=np.max(globals()[data][:,PD_num])    
            max_num[i]=max_value
            print(PD_num,data,i)
            i+=1
    return max_num

def draw_all_PD():
    for PD_num in np.arange(32):
        PD_data_1=find_siglePDmax_allData(PD_num,1)
        PD_data_2=find_siglePDmax_allData(PD_num,2)
        PD_data_3=find_siglePDmax_allData(PD_num,3)
        x=np.arange(15,80,2)
        plt.style.use("seaborn-poster")    
        fig1=plt.figure()
        plt.title("PD="+str(PD_num))
        plt.plot(x,PD_data_1,label='Times=1')
        plt.plot(x,PD_data_2,label='Times=2')
        plt.plot(x,PD_data_3,label='Times=3')
        plt.ylim((0,1500))
        plt.legend()
        plt.xticks(np.arange(10,80,1),fontsize=6)
        plt.grid(axis='x',linestyle='-.')
        plt.savefig("../Data/2019_8_23/picture/siglePD_15_79/"+str(PD_num)+".jpg")
        plt.close()
def devide_data_AllPD():
    save_path="../Data/2019_8_23/npy_singlePD_data/pd"
    for PD_num in np.arange(32):
        PD_data_1=find_siglePDmax_allData(PD_num,1)
        PD_data_2=find_siglePDmax_allData(PD_num,2)
        PD_data_3=find_siglePDmax_allData(PD_num,3)

        np.save(save_path+str(PD_num)+'_1',PD_data_1)
        np.save(save_path+str(PD_num)+'_2',PD_data_2)
        np.save(save_path+str(PD_num)+'_3',PD_data_3)
#    x=np.arange(15,80,2)
#    plt.style.use("seaborn-poster")    
#    fig1=plt.figure()
#    plt.title("PD="+str(PD_num))
#    plt.plot(x,PD_data_1,label='Times=1')
#    plt.plot(x,PD_data_2,label='Times=2')
#    plt.plot(x,PD_data_3,label='Times=3')
#    plt.ylim((0,1500))
#    plt.legend()
#    plt.savefig("../Data/2019_8_23/picture/siglePD_15_79/"+str(PD_num)+".jpg")
#    plt.close()

#%%

PD_num=20    
PD_data_1=find_siglePDmax_allData(PD_num,1)
PD_data_2=find_siglePDmax_allData(PD_num,2)
PD_data_3=find_siglePDmax_allData(PD_num,3)
#
x=np.arange(15,80,2)
plt.style.use("seaborn-poster")    
fig1=plt.figure()
plt.title("PD="+str(PD_num))
plt.plot(x,PD_data_1,label='Times=1')
plt.plot(x,PD_data_2,label='Times=2')
plt.plot(x,PD_data_3,label='Times=3')
plt.ylim((0,1500))
plt.xlim(10,80)
plt.xticks(np.arange(10,80,1),fontsize=6)
plt.grid(axis='x',linestyle='-.')
plt.legend()



