import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os

def load_AllFile():
    load_path="../Data/2019_8_23/npy_singlePD_data/"
    FileList=list(filter(lambda x:(x[-4:]==".npy"),os.listdir(load_path)))
    for file in FileList:
        var_name=file[0:-4]
        globals()[var_name]=np.load(load_path+file)
    return 0
load_AllFile()




#%%
#pd20_1[]

x=np.arange(33)
plt.style.use("seaborn-poster")    
fig1=plt.figure()
plt.plot(x,pd20_1)
plt.xticks(x,fontsize=10)
plt.grid(axis='x',linestyle='-.')

