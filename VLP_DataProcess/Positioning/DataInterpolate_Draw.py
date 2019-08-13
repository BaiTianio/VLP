# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:52:06 2019

@author: abc47
"""

import numpy as np
from scipy.interpolate import interp1d,interp2d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


#一维线性插值使用插值将数据矩阵转换成方阵
def d1Linear_interpol(in_data):
    row_num=in_data.shape[0]
    interpol_data=np.zeros((row_num,row_num))
    x=np.linspace(0,row_num,num=32)
    x_i=np.linspace(0,row_num,num=row_num)
    for i in range(row_num):
        f=interp1d(x,in_data[i,:],kind='linear')
        interpol_data[i]=f(x_i)
    return interpol_data

#二维样条插值
def d2Cubic_interpol(in_data):
    row_num=in_data.shape[0]
    column_num=in_data.shape[1]
    y=np.linspace(0,row_num,num=row_num)#列是x，行是y
    x=np.linspace(0,column_num,num=column_num)
    func = interp2d(x, y, in_data, kind='cubic')
    new_row=np.linspace(0,row_num,row_num*2)
    new_column=np.linspace(0,32,row_num*2)
    return func(new_column,new_row)



def draw_3d(in_data):
    
    in_data_row=in_data.shape[0]
    in_data_column=in_data.shape[1]
    
    fig=plt.figure(figsize=(4,4),dpi=300)
    
#    ax3 = fig.add_subplot(1,1,1,projection="3d")
    ax3 = plt.gca(projection='3d')
    
    #定义三维数据
#    y = np.linspace(0,in_data_row*in_data_column,num=in_data_row)
#    x = np.linspace(0,in_data_row*in_data_column,num=in_data_column)
    
    y = np.arange(in_data_row)
    x = np.arange(in_data_column)
    [X,Y]= np.meshgrid(x,y)#生成坐标网格
    Z = in_data
    
    #作图
    p=ax3.plot_surface(X,Y,Z,cmap='rainbow')
#    ax3.xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    
    #修改坐标轴
    plt.xticks(np.arange(0,x.shape[0]+1,int(x.shape[0]/6)),('0°','','30°','','60°','','90°'))
    plt.yticks(np.arange(0,y.shape[0]+1,int(y.shape[0]/6)),('0°','','120°','','240°','','360°'))
#    plt.yticks(np.arange(0,Y.shape[0]*1100,int(Y.shape[0]/4)*1100),('0°','120°','240°','360°'))
#    plt.colorbar(p)#显示色度条
    plt.xlabel("polor angle(x)",fontproperties="SimHei")
    plt.ylabel("horizontal(y)",fontproperties="SimHei")
    plt.draw()

def draw_2d(data):
    fig=plt.figure(figsize=(5,5),dpi=100)
    x = np.linspace(0,1,32)
    y = np.linspace(0,1,32)
    plt.plot(x,y)  

#draw_3d(d2Cubic_interpol_data)