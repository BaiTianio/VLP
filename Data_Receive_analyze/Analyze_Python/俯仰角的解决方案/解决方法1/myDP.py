# -*- coding: utf-8 -*-
#数据中要用的一些函数

import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#可用函数总结：

class Load_Save():#用于加载数据
    '''
    可以使用load_AllData加载数据文件夹中的所有数据
    '''
    #def __init__(self):
    @staticmethod
    def Load_All(**kargs):#加载所有数据到全局变量
        root=tk.Tk()
        root.withdraw()
        if('initialdir' in kargs.keys()):
            initialdir=kargs['initialdir']
        else:
            initialdir='C:/Users/abc47/Desktop/VLP/RotateVLP/Data_Receive_analyze/'
        load_path=filedialog.askdirectory(title='加载数据目录!!!look here',initialdir=initialdir)
        data_dict={}    
        FileList=list(filter(lambda x:(x[-4:]==".csv"),os.listdir(load_path)))
        for file in FileList:
            var_name=file[0:-4]
            data_dict[var_name]=np.array(pd.read_csv(load_path+'/'+file))#加载测量数据
        return data_dict
    
    @staticmethod
    def Load_files(**kwargs):#加载所有数据到全局变量
        root=tk.Tk()
        root.withdraw()
        if('initialdir' in kwargs.keys()):
            initialdir=kwargs['initialdir']
        else:
            initialdir='C:/Users/abc47/Desktop/VLP/RotateVLP/Data_Receive_analyze/'
        load_path=filedialog.askopenfiles(title='加载数据文件!!!look here',initialdir=initialdir)   
        data_dict={}
        for path in load_path: 
            var_name=path.name[-8:-4]
            data_dict[var_name]=np.array(pd.read_csv(path.name))#加载测量数据
        return data_dict
    @staticmethod
    def saveBox(
            title='save file',
            fileName=None,
            initialdir=None,
            fileExt=None,
            fileTypes=None,
            asFile=False):
        if fileTypes is None:
            fileTypes = [('all files', '.*'), ('text files', '.txt'),('JPEG/jpg', '.jpg')]
        # define options for opening
        options = {}
        options['defaultextension'] = fileExt
        options['filetypes'] = fileTypes
        options['initialdir'] = initialdir
        options['initialfile'] = fileName
        options['title'] = title

        if asFile:
            return filedialog.asksaveasfile(mode='w', **options)
        # will return "" if cancelled
        else:
            return filedialog.asksaveasfilename(**options) 
        
class save_data():
    def __init__(self):
            root=tk.Tk()
            root.withdraw()
            self.save_path=filedialog.askdirectory(title='保存数据目录!!!look here',initialdir='C:/Users/abc47/Desktop/VLP/RotateVLP/Data_Receive_analyze/Data_Picture/2019_8_23')
    def saveData_csv(self,data,filename):#使用csv保存数据
        if(type(data)!="<class 'pandas.core.frame.DataFrame'>"):
            data=pd.DataFrame(data)
        data.to_csv(self.save_path+"/{}.csv".format(filename),header=None,index=None)
        
        
#使用load_AngleData加载数据文件夹中的指定角度的数据
#    def load_AngleData(self,angle):#加载指定角度数据到全局变量
#        load_path=self.load_path
#        FileList=list(filter(lambda x:(x[5:7]==str(angle)),os.listdir(load_path)))
#        try:
#            for file in FileList:
#                var_name=file[0:-4]
#                if(FileList[0][-4:]=='.csv'):
#                    globals()[var_name]=np.array(pd.read_csv(load_path+'/'+file))#加载测量数据
#                elif(FileList[0][-4:]=='.npy'):
#                    print(var_name)
#                    globals()[var_name]=np.load(load_path+'/'+file)#加载测量数据
#        except(IndexError):
#            print("不存在的角度数据")


#数据处理常用的函数        
class DataProcess:

    @staticmethod
    def column_MaxValue(in_data):
        max_num=np.array([])    
        for i in range(in_data.shape[-1]):
            max_num=np.append(max_num,np.max(in_data[:,i]))    
        return max_num
    @staticmethod
    def column_MaxPosi(in_data):
        max_loc=np.int64([])    
        for i in range(in_data.shape[-1]):
            max_loc=np.append(max_loc,np.argmax(in_data[:,i]))    
        return max_loc
    
    # #从字典数据集中所有数据抽取指定的一列，一维二维都可以   
    # @staticmethod
    # def selectedPD_Data(PD_num,in_data):
    #     PD_data={}
    #     if(len(list(in_data.values())[0].shape)>1):
    #         for index in in_data.keys():
    #             PD_data[index]=in_data[index][:,PD_num]
    #     else:
    #         for index in in_data.keys():
    #             PD_data[index]=in_data[index][PD_num]
    #     return PD_data
#    
   
    
#load_inst=load_data()
#data=load_inst.load_AllData()    
class my_draw():
    
    @staticmethod
    def draw3d(data,**kargs):
#    '简化matplotlib 3D的画图'
        Z = data
        x=data.shape[0]
        y=data.shape[1]
        [X,Y]= np.meshgrid(np.arange(x),np.arange(y))#生成坐标网格 
         #绘图
        ax3 = fig.add_subplot(1,1,1,projection="3d")
        ax3.plot_surface(X,Y,Z,cmap='rainbow')
         #图形优化
        if(kargs['xticks']):
             plt.xticks(np.linspace(0,x-1,len(kargs['xticks']),dtype=np.int),kargs['xticks'])
        if(kargs['yticks']):
             plt.xticks(np.linspace(0,y-1,len(kargs['yticks']),dtype=np.int),kargs['yticks'])
        return 0

    def graph_adjust(**kargs):   
         #修改坐标轴
        if('xticks' in kargs):
             plt.xticks(np.linspace(0,kargs['x_scale']-1,len(kargs['xticks']),dtype=np.int),kargs['xticks'])
        if('yticks' in kargs):
             plt.yticks(np.linspace(0,kargs['y_scale']-1,len(kargs['yticks']),dtype=np.int),kargs['yticks'])
             
        if('ticks_size' in kargs):
             plt.xticks(fontsize=kargs['ticks_size'])    
             plt.yticks(fontsize=kargs['ticks_size'])    
        return 0
    
    def font_config(**kargs):
        if('size' not in kargs):
            kargs['size']=10
        font = {'family' : 'SimHei',
                'weight' : 'normal',
                'size'   : kargs['size']}
        plt.rc('font', **font)               # 步骤一（设置字体的更多属性）
        plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）  
        return 0
    
    def draw_siglePD_save(in_data,PD_num,save_path):
        plt.style.use("seaborn-paper")
        plt.figure(figsize=(16,10),dpi=300)
        for times in range(3):
            plt.plot(in_data[times],label="times="+str(times+1))
        plt.title("PD="+str(PD_num))
        plt.legend()
        plt.savefig(save_path+"/PD"+str(PD_num)+'.png')
        plt.close()   
            
#    def draw_32PD(angles,save_path):
#    plt.style.use("seaborn-paper")
#    print(save_path)
#    for angle in angles:
#        for times in range(1,4):
#            vari_name='data_{}_{}'.format(angle,times)
#            data=globals()[vari_name]
#            plt.figure(figsize=(16,10),dpi=300)
#            for PD_num in np.arange(int((angle-7.5)/2.5)-4,int((angle-7.5)/2.5)+4):
#                plt.plot(data[:,PD_num],label='PD='+str(PD_num))
#            plt.title("Angle=%s"%angle)
#            plt.legend()
#            plt.savefig(save_path+"/angle{}_{}.png".format(angle,times))
#            plt.close()   