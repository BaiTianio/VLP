
#根据不同的数据特征来调整增益
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm


from func_pack import load_data,data_Process





if('all_data' not in globals()):
    load_data=load_data()
    all_data=load_data.load_AllData()

norm_data=data_Process.normalize(all_data)

PD_time1=
PD_AllAngle={}
for PD_num in range(0,32):
    for times in range(1,4):
        PD_AllAngle['PD{}_{}'.format(PD_num,times)]=data_Process.selectedPD_Data(PD_num,norm_data[index])




##求所有数据中，每个PD的最大值
#PD_max={}
#for PD_num in range(1,33):
#    signlePD_data=data_Process.selectedPD_Data(PD_num,all_data)
#    temp=np.array([])
#    for data in signlePD_data.values():
#        temp=np.append(temp,data[np.argpartition(data,len(data)-100)[-100:]])
#        PD_max[PD_num]=temp[np.argpartition(temp,len(temp)-100)[-100:]].mean()
# 
    
#输出保存增益调整后的数据  
#定义每个PD的增益调整系数
#gain_coeff=(964,1246,1136,1018,1350,1523,1371,1770,2063,1420,1346,1310,1253,1158,1181,1271,997,879,1014,
#1102,1136,933,952,936,838,928,927,842,880,918,967,777)    
#root=tk.Tk()
#root.withdraw()
#save_path=filedialog.askdirectory()
#
#for index in all_data.keys():
#    for PD_num in range(1,33):
#        all_data[index][:,PD_num]/=gain_coeff[PD_num-1]
#    pd.DataFrame(all_data[index]).to_csv(save_path+'/'+index+'.csv')