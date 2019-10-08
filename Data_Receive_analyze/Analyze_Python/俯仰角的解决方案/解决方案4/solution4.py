# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:48:28 2019

@author: abc47
"""
import numpy as np
import os
import matplotlib.pyplot as plt 
import myDP
from scipy.optimize import leastsq

def residuals(p,x, y):
#    fun = lambda x: p[0]*(x**2)+p[1]*x+p[2]  # poly1d（）函数可以按照输入的列表p返回一个多项式函数 
    fun=np.poly1d(p)
    print(p)
    return y - fun(x)

# 拟合函数
def fitting(p,X,Y):
    pars = np.arange(0,p+1)  # 生成p+1个随机数的列表，这样poly1d函数返回的多项式次数就是p
    r = leastsq(residuals, pars, args=(X, Y))   # 三个参数：误差函数、函数参数列表、数据点
    return r
        
#load_data=myDP.Load_Save.Load_files(initialdir=os.getcwd()+'/')
    
x=[[0,0,0],[1,1,1],[2,2,2],[3,3,3]]
y=[0,1,2,3]
resu=fitting(2,x,y)
