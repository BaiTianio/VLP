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
    for i in range(100):
        if(data_in[i]==0 and data_in[i+9]==1 and data_in[i+27]==3 and data_in[i+36]==4):#判断四个数确保正确
            data_in=data_in[i:]
            print(i)
            break
    row_num=len(data_in)%9
    find_data=data_in[0:len(data_in)-row_num]
    data_storge=find_data.reshape(int(len(find_data)/9),9)
    for x in data_storge[:,0]:
        if(x>7):
            raise Exception("arrange error")
         
    #数值计算
    calculate_data=np.zeros((data_storge.shape[0],5))   
    calculate_data[:,0]=data_storge[:,0]
    calculate_data[:,1]=data_storge[:,1]*256+data_storge[:,2]
    calculate_data[:,2]=data_storge[:,3]*256+data_storge[:,4]
    calculate_data[:,3]=data_storge[:,5]*256+data_storge[:,6]
    calculate_data[:,4]=data_storge[:,7]*256+data_storge[:,8]
    
    #保证完整的帧
    calculate_data=calculate_data[0:-int(calculate_data[-1,0])-1,:] 
    #
    #原始数据采集顺序是3214，现需修改为1234排列
    calculate_data[:,[1,2,3,4]]=calculate_data[:,[3,2,1,4]]
    PD32_data=calculate_data[:,1:5].reshape((-1,32))
    return PD32_data


#def read_AllData():
load_path="../Data/2019_8_23/npy_raw_select/"
save_npy_path="../Data/2019_8_23/npy_arranged/"
save_csv_path="../Data/2019_8_23/csv_arranged/"

Req_FileList=list(filter(lambda x:(x[-4:]==".npy"),os.listdir(load_path)))

for file in Req_FileList:
    var_name=file[0:-4]
    locals()[var_name]=np.load(load_path+file)
    locals()[var_name]=arrange_data(locals()[var_name])
#    np.save(save_npy_path+str(var_name)+'.npy',locals()[var_name])
#    locals()[var_name+'_df']=pd.DataFrame(locals()[var_name])
#    locals()[var_name+'_df'].to_csv(save_csv_path+var_name+'.csv')
    
    
    
    
#    exec("np.save(save_npy_path+'{}.npy',temp)".format(var_name),locals(),globals())
     
#for file in Req_FileList:
#    var_name=file[0:-4]
#    exec(var_name+'=np.load(load_path+file)',locals(),globals())
#    arrange_data(data_in)
##    exec("np.save(save_path+'{}.npy',{})".format(var_name,var_name),locals(),globals())
##    exec('{}_df=pd.DataFrame({})'.format(file[0:-4],file[0:-4]),locals(),globals())
##    exec( var_name+"_df"+".to_csv('{}{}.csv')".format(save_path,var_name),locals(),globals())

    

