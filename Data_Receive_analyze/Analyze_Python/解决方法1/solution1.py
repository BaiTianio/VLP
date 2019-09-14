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

load_data=myDP.Data_Load_Save.Load_files(initialdir=os.getcwd())
max_col=myDP.DataProcess.column_MaxValue(load_data['45_1'][:,1:])


def colum_rearrange(data_in):
    
    