# coding:utf-8
#import numpy as np
#from tkinter.filedialog import *
#import tkinter

import numpy as np


from GetData_From_Wifi     import get_wifi_data
from ArrangeData           import data_arrange
from DataInterpolate_Draw  import d2Cubic_interpol,draw_3d
from Positioning           import find_Extreme,FindAll_ExtremePoint

import pandas as pd
#import time

#将DataFrame存储为csv,index表示是否显示行名，default=True


#获取数据
#i=0
#while(i<20):
#    raw_data=get_wifi_data()
#    np.save(os.getcwd()+"\\raw_data\\data_%d.npy"%i,raw_data)
#    i=i+1
#    print("第%d次接收完成"%i)
#    time.sleep(10)
#raw_data=np.load(os.getcwd()+"\\raw_data\\data_%d.npy"%4)
#%%
raw_data=np.load("./raw_data_1,2.npy")
arranged_data=data_arrange(raw_data)
#%%
#path="./data/lantcTest_ALLArray_2."
raw_data=get_wifi_data() 
np.save("raw_data_1,4.npy",raw_data)

#arranged_data=data_arrange(raw_data)
#np.sipbdave(path+"npy",arranged_data)
#dataframe=pd.DataFrame(arranged_data)
#dataframe.to_csv(path+"csv",index=False,sep=',')
#test_value=arranged_data[:,6].mean()
#test_data=arranged_data
#draw_3d(arranged_data)
#d2Cubic_interpol_data=d2Cubic_interpol(arranged_data)
#draw_3d(d2Cubic_interpol_data)
#
#FindAll_ExtremePoint(d2Cubic_interpol_data)

#finded_data,max_index=find_Extreme(d2Cubic_interpol_data)
#draw_3d(finded_data)
#np.save("raw_data.npy",d2Cubic_interpol_data)
#np.savetxt("raw_data.csv",d2Cubic_interpol_data)
#d1Linear_interpol_data=d1Linear_interpol(formed_data)
#d2Cubic_interpol_data=d2Cubic_interpol(formed_data)
#draw_3d(d2Cubic_interpol_data)
#final_data=find_Extreme(d2Cubic_interpol_data)
#draw_3d(final_data)