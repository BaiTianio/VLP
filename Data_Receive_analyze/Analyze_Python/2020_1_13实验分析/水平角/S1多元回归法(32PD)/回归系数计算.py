# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:07:07 2020

@author: abc47
"""
import os
import numpy as np
from scipy.optimize import leastsq
import re
#定义拟合函数
def func(p,x):
    y=np.dot(x*x,p.T)
    return y
    
#定义损失函数
def residuals(p,x, y):
    res= y - func(p,x)
    print(res)
    return res


#数据准备
LoadPath="./数据/"
FileList=list(filter(lambda x:(x[-6:]=="_0.npy"),os.listdir(LoadPath)))
data_stroge=np.zeros([len(FileList),32])
angle_stroge=np.zeros(len(FileList))
cout=0
for file in FileList:
    data_stroge[cout]=np.load(LoadPath+file)
    pattern=r",{1}.*\)"
    angle_temp=int(re.search(pattern,file).group()[1:-1])+20
    angle_stroge[cout]=angle_temp
    cout+=1    

init_pars=np.ones(32)
# 拟合函数
pars= leastsq(residuals, init_pars, args=(data_stroge,angle_stroge))[0]   # 三个参数：误差函数、函数参数列表、数据点
