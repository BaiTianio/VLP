import numpy as np
import os
import pandas as pd

def column_max(in_data):
    max_num=np.int64([])    
    for i in range(in_data.shape[1]):
        max_num=np.append(max_num,np.max(in_data[:,i]))    
    return max_num
def column_maxposi(in_data):
    max_loc=np.int64([])    
    for i in range(in_data.shape[1]):
        max_loc=np.append(max_loc,np.argmax(in_data[:,i]))    
    return max_loc

def arrange_data(data_in):
    for i in range(32):
        if(data_in[i]==0 and data_in[i+9]==1 and data_in[i+18]==2 and data_in[i+27]==3):
            data_in=data_in[i:]
            print(i)
    row_num=len(data_in)%9
    find_data=data_in[0:len(data_in)-row_num]
    data_storge=find_data.reshape(int(len(find_data)/9),9)
    for x in data_storge[:,0]:
        if(x>7):
            raise Exception("arrange error")
    #数值计算
    calculate_data=np.c_[data_storge[:,0],data_storge[:,1]*256+data_storge[:,2]]
    calculate_data=np.c_[calculate_data,data_storge[:,3]*256+data_storge[:,4]]
    calculate_data=np.c_[calculate_data,data_storge[:,5]*256+data_storge[:,6]]
    calculate_data=np.c_[calculate_data,data_storge[:,7]*256+data_storge[:,8]]
    
    #原始数据采集顺序是3214，现需修改为1234排列
    calculate_data[:,[1,2,3,4]]=calculate_data[:,[3,2,1,4]]
    PD32_data=calculate_data[:,1:5].reshape((-1,32))
    return PD32_data

#def read_AllData():
load_path="../Data/data_8_23/"
save_path="../Data/data_8_23_csv/"
All_FileList=os.listdir(load_path)
Req_FileList=list(filter(lambda x:(x[-4:]==".npy"),All_FileList))

for file in Req_FileList:
    var_name=file[0:-4]
    exec(var_name+'=np.load(load_path+file)',locals(),globals())
    exec('{}_df=pd.DataFrame({})'.format(file[0:-4],file[0:-4]),locals(),globals())
    exec( var_name+"_df"+".to_csv('{}{}.csv')".format(save_path,var_name),locals(),globals())
#    return 0

#read_AllData()
#max_value=column_max(PD32_data)


#np.zeros([int(calculate_data.shape[0]/8),32])
#for i in range(32):
#    PD32_data[i]=calculate_data[0:-1:7,0]

#data_in=calculate_data
#row_num=int(data_in.shape[0]/8)
#PDarray_data=np.zeros((row_num,8))

#for i in range(row_num):  
#    if(data_in[i*8,0]==0 and data_in[i*8+7,0]==7):
#        PDarray_data[i,:]=data_in[i*8:(i+1)*8,group_num].T  




#angle=79
#for times in range(5):



#def data_arrange(data_in):
#    #用于除去数据头部不完整帧的数据
#    for i in range(27):
#        if( data_in[i]==0     and data_in[i+9]==1  and 
#            data_in[i+18]==2  and data_in[i+27]==3 ):
#            data_in=data_in[i:]
#            row_num=len(data_in)%9
#            find_data=data_in[0:len(data_in)-row_num]
#            data_storge=find_data.reshape(int(len(find_data)/9),9)
#            break
#     
#     #检查数据中索引是否出错
#    for x in data_storge[:,0]:
#        if(x>7):
#            raise Exception("arrange error")
#     
#    calculate_data=np.c_[data_storge[:,0],data_storge[:,1]*256+data_storge[:,2]]
#    calculate_data=np.c_[calculate_data,data_storge[:,3]*256+data_storge[:,4]]
#    calculate_data=np.c_[calculate_data,data_storge[:,5]*256+data_storge[:,6]]
#    calculate_data=np.c_[calculate_data,data_storge[:,7]*256+data_storge[:,8]]  
#    def data_divide_group(data_in,group_num):  
#        
#        row_num=int(data_in.shape[0]/8)
#        PDarray_data=np.zeros((row_num,8))
#        #½«ËùÓÐÊý¾Ý°´ÕÕPDÕóÁÐ½øÐÐ·Ö×é
#        for i in range(row_num):  
#            if(data_in[i*8,0]==0 and data_in[i*8+7,0]==7):
#                PDarray_data[i,:]=data_in[i*8:(i+1)*8,group_num].T  
#                
#        PDarrayGroup_data=np.c_[PDarray_data[:,0],PDarray_data[:,1],PDarray_data[:,2],PDarray_data[:,3],
#                                PDarray_data[:,4],PDarray_data[:,5],PDarray_data[:,6],PDarray_data[:,7]]
#        return PDarrayGroup_data
#    
#    #ÕýÈ·½Ç¶ÈÅÅÁÐÓ¦ÎªCBAD£¨3214£© 
#    PDarrayA_DataGroup=data_divide_group(calculate_data,3)#ÆðÊ¼Î»ÖÃ0
#    PDarrayB_DataGroup=data_divide_group(calculate_data,2)#ÆðÊ¼Î»ÖÃ-1/4
#    PDarrayC_DataGroup=data_divide_group(calculate_data,1)#ÆðÊ¼Î»ÖÃ-2/4
#    PDarrayD_DataGroup=data_divide_group(calculate_data,4)#ÆðÊ¼Î»ÖÃ-3/4
#    
#    PDarrayB_DataGroup=np.roll(PDarrayB_DataGroup,int(PDarrayB_DataGroup.shape[0]*3/4),axis=0)#½«B×éÊý¾ÝÑ­»·ÓÒÒÆ3/4,Ïàµ±ÓÚÑ­»·×óÒÆ1/4
#    PDarrayC_DataGroup=np.roll(PDarrayC_DataGroup,int(PDarrayC_DataGroup.shape[0]*2/4),axis=0)#½«C×éÊý¾ÝÑ­»·ÓÒÒÆ2/4£¬Ïàµ±ÓÚÑ­»·×óÒÆ2/4
#    PDarrayD_DataGroup=np.roll(PDarrayD_DataGroup,int(PDarrayD_DataGroup.shape[0]*1/4),axis=0)#½«C×éÊý¾ÝÑ­»·ÓÒÒÆ1/4£¬Ïàµ±ÓÚÑ­»·×óÒÆ3/4
#    
#    
#    #Êý¾Ý´©²åÕûºÏ
#    row_num=np.max([PDarrayA_DataGroup.shape[0],PDarrayB_DataGroup.shape[0],
#                   PDarrayC_DataGroup.shape[0],PDarrayD_DataGroup.shape[0]])
#    data_summary=np.zeros((row_num,32))
#    for i in range(8):
#        data_summary[:,i*4]=PDarrayA_DataGroup[:,i]
#        data_summary[:,i*4+1]=PDarrayB_DataGroup[:,i]
#        data_summary[:,i*4+2]=PDarrayC_DataGroup[:,i]
#        data_summary[:,i*4+3]=PDarrayD_DataGroup[:,i]
#    return data_summary    
##data_cross=np.zeros()
##for i in arange(calculate_data.size):
#    
#raw_data=np.load("../Data/data_8_23/data_67_1.npy")
#arranged=data_arrange(raw_data)
    

