# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:48:28 2019

@author: abc47
"""
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt 
from scipy.stats import norm
import myDP
import tkinter as tk
from tkinter import filedialog

load_data=myDP.Load_Save.Load_files(initialdir=os.getcwd()+'/')
max_col=myDP.DataProcess.column_MaxValue(list(load_data.values())[0][:,1:])

def data_select(data_in):
    selected_data=[]
    pd_select=[ 7, 8,10,12,15,
               13,16,19,17,20,
               23,21,24,26,25,28]
    for pd_num in pd_select:
        selected_data.append(data_in[pd_num])
    return selected_data
pd_select=data_select(max_col)
plt.plot(pd_select)
filename=list(load_data.keys())[0]
plt.title(filename)
savePath=myDP.Load_Save.saveBox(initialdir=os.getcwd(),fileName=filename)
plt.savefig(savePath)
plt.close()
        