# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 20:19:39 2019

@author: abc47
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os

def read_data():
    path="../Data/data_csv/"
    file_list=os.listdir(path)
    for file_name in file_list:
        eval(file_name[0:-4]+"=np.array(pd.read_csv(path+file_name))")  
    return data
