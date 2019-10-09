# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:48:28 2019

@author: abc47
"""
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import leastsq
import pandas as pd
import os

#定义拟合函数
def func(p,x):
    y=np.dot(x,p.T)
    return y
    
#定义损失函数
def residuals(p,x, y):
    res= y - func(p,x)
    print(res)
    return res


#数据准备
def Load_All():#加载所有数据
    load_path=r"./数据/每个数据取列最大值/"
    load_data=np.zeros((33,32))    
    for index_num in range(33):
        index='data_'+str(index_num*2+15)+'_1.csv'
        read_data=np.array(pd.read_csv(load_path+index,header=None)).T
        load_data[index_num]=read_data#加载测量数据
    return load_data


X=Load_All()        
Y=np.arange(15,80,2)

pars=np.linspace(1,1,32)
# 拟合函数
r= leastsq(residuals, pars, args=(X, Y))[0]   # 三个参数：误差函数、函数参数列表、数据点

for index_num in range(33):
    angle=func(r,X[index_num])
    print(angle)
