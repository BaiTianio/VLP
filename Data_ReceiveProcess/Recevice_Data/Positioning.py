# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:37:15 2019

@author: abc47
"""
import numpy as np

from DataInterpolate_Draw  import d2Cubic_interpol,draw_3d

#def FindAll_ExtremePoint(data_in):
#    ExtrePLocal=np.zeros((5,2))#创造一个数组用来存储极值点
#    for i in range(5):
#        data_in,ExtrePLocal[i,:]=find_Extreme(data_in)
#        draw_3d(data_in)
#        print()
#    return data_in,ExtrePLocal
 
def FindAll_ExtremePoint(data_in):
#    ExtrePLocal=np.zeros((5,2))#创造一个数组用来存储极值点
    for i in range(5):
        data_in,ExtrePLocal=find_Extreme(data_in)
        draw_3d(data_in)
        print(ExtrePLocal)
        
def find_Extreme(data_in):
    range_row=int(data_in.shape[0]/30)#计算行列的比例范围
    range_column=int(data_in.shape[1]/30)
    (max_row,max_column)=np.unravel_index(data_in.argmax(),data_in.shape)#找出最值所在的坐标
    if __name__ == "__main__":
        print(max_row,max_column)
    
    findRow_start=max_row-range_row
    findRow_end=max_row+range_row
    findColumn_start=max_column-range_column
    findColumn_end=max_column+range_column
   
    if(findRow_start<0):
        findRow_start=0
    if(findRow_end>=data_in.shape[0]):
        findRow_end=data_in.shape[0]
    if(findColumn_start<0):
        findColumn_start=0
    if(findColumn_end>=data_in.shape[1]):
        findColumn_end=data_in.shape[1]

    for row_temp in range(findRow_start,findRow_end):
        for column_temp in range(findColumn_start,findColumn_end):
            data_in[row_temp,column_temp]=0
    return data_in,(max_row,max_column)
#
#data=np.load("raw_data.npy")
#finded_data,max_point=find_Extreme(data)