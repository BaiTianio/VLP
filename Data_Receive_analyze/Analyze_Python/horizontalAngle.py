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
import tkinter as tk
from tkinter import filedialog
from multiprocessing import Process,Pool

#with open("./数据保存文件夹地址.txt",'r+') as path_file:
#    path=path_file.read()
#    
#root=tk.Tk()
#root.withdraw()
#newpath=filedialog.askdirectory()
#%%
def load_AllFile():
    try:
        with open("./数据保存文件夹地址.txt",'r+') as path_file:
            load_path=path_file.read()
            print(load_path)  
        FileList=list(filter(lambda x:(x[-4:]==".csv"),os.listdir(load_path)))
        for file in FileList:
            var_name=file[0:-4]
            globals()[var_name]=np.array(pd.read_csv(load_path+'/'+file))#加载测量数据
        return 0
    except(FileNotFoundError):
        root=tk.Tk()
        root.withdraw()
        newpath=filedialog.askdirectory()
        with open("./数据保存文件夹地址.txt",'w+') as path_file:
            load_path=path_file.write(newpath)
            return 0
load_AllFile()
#%%

def draw_32PD(angles,save_path):
    plt.style.use("seaborn-paper")
    print(save_path)
    for angle in angles:
        for times in range(1,4):
            vari_name='data_{}_{}'.format(angle,times)
            data=globals()[vari_name]
            plt.figure(figsize=(16,10),dpi=300)
            for PD_num in np.arange(int((angle-7.5)/2.5)-4,int((angle-7.5)/2.5)+4):
                plt.plot(data[:,PD_num],label='PD='+str(PD_num))
            plt.title("Angle=%s"%angle)
            plt.legend()
            plt.savefig(save_path+"/angle{}_{}.png".format(angle,times))
            plt.close()   
if __name__ == '__main__':            
    root=tk.Tk()
    root.withdraw()
    save_path=filedialog.askdirectory()
    
    p=Pool()
    for i in np.arange(25,66,10):
        p.apply_async(draw_32PD, args=(np.arange(i,i+10,2),save_path))
    p.close()
    p.join()


