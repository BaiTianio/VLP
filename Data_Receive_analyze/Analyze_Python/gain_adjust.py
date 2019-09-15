
#根据不同的数据特征来调整增益
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm


from func_pack import load_data,data_Process


PD_max=(995, 1273, 1186, 1053, 1378, 1564, 1442, 1804, 2123, 1446, 1389, 1337,
 1289, 1177, 1229, 1286, 1033,  895, 1047, 1118, 1152,  950,  986,  950,
  855,  945,  944,  892,  911,  936,  984,  783)



#读取数据
if('all_data' not in globals()):
    load_data=load_data()
    all_data=load_data.load_AllData()

#生成增益调整的数据
  

#PD_time1=
#PD_AllAngle={}
#for PD_num in range(0,32):
#    for times in range(1,4):
#        PD_AllAngle['PD{}_{}'.format(PD_num,times)]=data_Process.selectedPD_Data(PD_num,norm_data[index])



