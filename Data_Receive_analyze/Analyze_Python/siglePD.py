# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 20:19:39 2019

@author: abc47
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from func_pack import load_data


def find_siglePDmax_allData(PD_num,time):
    max_num=np.zeros(33)
    pattern=re.compile("data_\d+?_{}".format(time))
    loca_var=list(globals())
    i=0
    for data in loca_var:
        if(re.match(pattern,data)):
            max_value=np.max(globals()[data][:,PD_num])    
            max_num[i]=max_value
            print(PD_num,data,i)
            i+=1
    return max_num

def draw_all_PD():
    for PD_num in np.arange(32):
        PD_data_1=find_siglePDmax_allData(PD_num,1)
        PD_data_2=find_siglePDmax_allData(PD_num,2)
        PD_data_3=find_siglePDmax_allData(PD_num,3)
        x=np.arange(15,80,2)
        plt.style.use("seaborn-poster")    
        fig1=plt.figure()
        plt.title("PD="+str(PD_num))
        plt.plot(x,PD_data_1,label='Times=1')
        plt.plot(x,PD_data_2,label='Times=2')
        plt.plot(x,PD_data_3,label='Times=3')
        plt.ylim((0,1500))
        plt.legend()
        plt.xticks(np.arange(10,80,1),fontsize=6)
        plt.grid(axis='x',linestyle='-.')
        plt.savefig("../Data/2019_8_23/picture/siglePD_15_79/"+str(PD_num)+".jpg")
        plt.close()
def devide_data_AllPD():
    save_path="../Data/2019_8_23/npy_singlePD_data/pd"
    for PD_num in np.arange(32):
        PD_data_1=find_siglePDmax_allData(PD_num,1)
        PD_data_2=find_siglePDmax_allData(PD_num,2)
        PD_data_3=find_siglePDmax_allData(PD_num,3)

        np.save(save_path+str(PD_num)+'_1',PD_data_1)
        np.save(save_path+str(PD_num)+'_2',PD_data_2)
        np.save(save_path+str(PD_num)+'_3',PD_data_3)
#    x=np.arange(15,80,2)
#    plt.style.use("seaborn-poster")    
#    fig1=plt.figure()
#    plt.title("PD="+str(PD_num))
#    plt.plot(x,PD_data_1,label='Times=1')
#    plt.plot(x,PD_data_2,label='Times=2')
#    plt.plot(x,PD_data_3,label='Times=3')
#    plt.ylim((0,1500))
#    plt.legend()
#    plt.savefig("../Data/2019_8_23/picture/siglePD_15_79/"+str(PD_num)+".jpg")
#    plt.close()
#%%

#def data2draw(PD_num):
#    x=np.arange(15,80,2)
#    PD_data_1=find_siglePDmax_allData(PD_num,1)
#    PD_data_2=find_siglePDmax_allData(PD_num,2)
#    PD_data_3=find_siglePDmax_allData(PD_num,3)
#    #
#    ideal_data=np.zeros([33,33])
#    for i in range(33):
#        ideal_data[:,i]=normal(mean=i)
#    oneangel=ideal_data[PD_num,:]*PD_data_1.max() 
#    
#    plt.plot(x,PD_data_1,label='real value times=1')
#    plt.plot(x,PD_data_2,label='real value times=2')
#    plt.plot(x,PD_data_3,label='real value times=3')
#    #图形设置
#    plt.plot(x,oneangel,label='ideal value')
#    plt.title("PD="+str(PD_num))
#    plt.grid(axis='x',linestyle='-.')
#    plt.ylim((0,1500))
#    plt.xlim(10,80)
#    plt.xlabel("AOA俯仰角($\degree$)")
#    plt.ylabel("光照度(lux)")
#    plt.xticks(np.arange(10,80,1),fontsize=6)
#    plt.legend()
#
#
#plt.style.use("seaborn-paper") 
#fig=plt.figure(dpi=300,figsize=(8,8))
#plt.subplot(311)
#data2draw(16)
#plt.subplot(312)
#data2draw(17)
#plt.subplot(313)
#data2draw(18)
#fig.tight_layout()#调整整体空白
#plt.subplots_adjust(wspace =0, hspace =0.4)
#plt.savefig('./temp.png')
#plt.close()


load_inst=load_data()
data=load_inst.load_AllData()
   




