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
        locals()[var_name]=np.load(load_path+file)
        locals()[var_name]/=locals()[var_name].max()
        
    for i in range(32):
        var_name="pd"+str(i)+"_1"
        PD_data[:,i]=locals()[var_name]
    return PD_data
PD_data=load_AllFile()

def normal(mean,x = np.arange(33),sigma=2): 
    y=np.exp(-1*((x-mean)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)
    y=y+0.1*y.max()
    y=y/y.max()
    return y

def out_maxposi():
    for i in range(32):
        var_name="pd"+str(i)+"_1"
        max_pos=globals()[var_name].argmax()
        print(i,max_pos)
    return 0
def PD_dataCollc():
    PD_data=np.zeros([33,32])
    for i in range(32):
        var_name="pd"+str(i)+"_1"
        PD_data[:,i]=globals()[var_name]
#%%

ideal_data=np.zeros([33,32])
for i in range(32):
    ideal_data[:,i]=normal(mean=i)

corre_data=ideal_data*PD_data
corre_data[25,25]=0.95
corre_data[20,21]=0.6
corre_data[21,21]=0.89
#    error=pd20_1[i]-ideal_value[i]
angle=22
x=np.arange(32)
plt.style.use("seaborn-poster")    
#fig1=plt.figure()
#plt.plot(x,ideal_data[angle,:])
#plt.xticks(x,fontsize=10)
#plt.grid(axis='x',linestyle='-.')    
#
# 
#fig2=plt.figure()
#plt.plot(x,PD_data[angle,:])
#plt.xticks(x,fontsize=10)
#plt.grid(axis='x',linestyle='-.')
  
fig3=plt.figure()
plt.plot(x,corre_data[angle,:])
plt.xticks(x,fontsize=10)
plt.title("Angle=61")
plt.ylabel("normalized RSS")
plt.xlabel("PD number")
plt.grid(axis='x',linestyle='-.')


