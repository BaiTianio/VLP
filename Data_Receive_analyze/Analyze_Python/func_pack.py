# -*- coding: utf-8 -*-
#数据中要用的一些函数

import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd
import numpy as np

class load_data():#加载所有数据到全局变量
    def __init__(self):
            root=tk.Tk()
            root.withdraw()
            self.load_path=filedialog.askdirectory()
    def load_AllData(self):
        load_path=self.load_path
        FileList=os.listdir(load_path)
        if(FileList[0][-4:]=='.csv'):
            for file in FileList:
                var_name=file[0:-4]
                globals()[var_name]=np.array(pd.read_csv(load_path+'/'+file))#加载测量数据
        elif(FileList[0][-4:]=='.npy'):
            for file in FileList:
                var_name=file[0:-4]
                globals()[var_name]=np.load(load_path+'/'+file)#加载测量数据
        return 0

    def load_AngleData(self,angle):#加载指定角度数据到全局变量
        load_path=self.load_path
        FileList=list(filter(lambda x:(x[5:7]==angle),os.listdir(load_path)))
        if(FileList[0][-4:]=='.csv'):
            for file in FileList:
                var_name=file[0:-4]
                globals()[var_name]=np.array(pd.read_csv(load_path+'/'+file))#加载测量数据
        elif(FileList[0][-4:]=='.npy'):
            for file in FileList:
                var_name=file[0:-4]
                globals()[var_name]=np.load(load_path+'/'+file)#加载测量数据
        return 0
load=load_data()
load.load_AllData()