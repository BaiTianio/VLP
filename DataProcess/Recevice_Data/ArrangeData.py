# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:25:48 2019

@author: abc47
"""
import numpy as np
#import matplotlib.pyplot as plt
#from scipy.fftpack import fft,ifft
#from scipy import signal

#����������
#data_in=np.load("raw_data.npy")

def data_arrange(data_in):
        
    #Ѱ�����ݵ�֡ͷ
    for i in range(len(data_in)-27):
        if( data_in[i]==0     and data_in[i+9]==1  and 
            data_in[i+18]==2  and data_in[i+27]==3 ):
            data_in=data_in[i:]
            row_num=len(data_in)%9#��֤���������ų�n��9�е���ʽ
            find_data=data_in[0:len(data_in)-row_num]
            data_storge=find_data.reshape(int(len(find_data)/9),9)
            break
     
     #���֡ͷ�����Ƿ����ִ���   
    for x in data_storge[:,0]:
        if(x>7):
            raise Exception("�����������")
     
    ##---------------������ӵõ�������ֵ---------------------------   
    calculate_data=np.c_[data_storge[:,0],data_storge[:,1]*256+data_storge[:,2]]
    calculate_data=np.c_[calculate_data,data_storge[:,3]*256+data_storge[:,4]]
    calculate_data=np.c_[calculate_data,data_storge[:,5]*256+data_storge[:,6]]
    calculate_data=np.c_[calculate_data,data_storge[:,7]*256+data_storge[:,8]]
    
    #    np.save("raw_data.npy",calculate_data)
    
    #ȷ��������֡����������������ÿ��PD�����ݳ�ȡ��������һ��PD�����ݱ���Ϊһ��group������
    def data_divide_group(data_in,group_num):  
        row_num=int(data_in.shape[0]/8)
        PDarray_data=np.zeros((row_num,8))
        #���������ݰ���PD���н��з���
        for i in range(row_num):  
            if(data_in[i*8,0]==0 and data_in[i*8+7,0]==7):
                PDarray_data[i,:]=data_in[i*8:(i+1)*8,group_num].T  
                
        PDarrayGroup_data=np.c_[PDarray_data[:,0],PDarray_data[:,1],PDarray_data[:,2],PDarray_data[:,3],
                                PDarray_data[:,4],PDarray_data[:,5],PDarray_data[:,6],PDarray_data[:,7]]
        return PDarrayGroup_data
    
    #��ȷ�Ƕ�����ӦΪCBAD��3214�� 
    PDarrayA_DataGroup=data_divide_group(calculate_data,3)#��ʼλ��0
    PDarrayB_DataGroup=data_divide_group(calculate_data,2)#��ʼλ��-1/4
    PDarrayC_DataGroup=data_divide_group(calculate_data,1)#��ʼλ��-2/4
    PDarrayD_DataGroup=data_divide_group(calculate_data,4)#��ʼλ��-3/4
    
    PDarrayB_DataGroup=np.roll(PDarrayB_DataGroup,int(PDarrayB_DataGroup.shape[0]*3/4),axis=0)#��B������ѭ������3/4,�൱��ѭ������1/4
    PDarrayC_DataGroup=np.roll(PDarrayC_DataGroup,int(PDarrayC_DataGroup.shape[0]*2/4),axis=0)#��C������ѭ������2/4���൱��ѭ������2/4
    PDarrayD_DataGroup=np.roll(PDarrayD_DataGroup,int(PDarrayD_DataGroup.shape[0]*1/4),axis=0)#��C������ѭ������1/4���൱��ѭ������3/4
    
    
    #���ݴ�������
    row_num=np.max([PDarrayA_DataGroup.shape[0],PDarrayB_DataGroup.shape[0],
                   PDarrayC_DataGroup.shape[0],PDarrayD_DataGroup.shape[0]])
    data_summary=np.zeros((row_num,32))
    for i in range(8):
        data_summary[:,i*4]=PDarrayA_DataGroup[:,i]
        data_summary[:,i*4+1]=PDarrayB_DataGroup[:,i]
        data_summary[:,i*4+2]=PDarrayC_DataGroup[:,i]
        data_summary[:,i*4+3]=PDarrayD_DataGroup[:,i]
    return data_summary    
    
    
#
##���鳤�ȵ����⣬�ڷָ�ʱ���ܲ������ȳ��ķָ��Σ����ȡ���зָ��ε���С����     
#row_num_temp=np.min([PDarray1_DataGroup[0].shape[0],PDarray1_DataGroup[1].shape[0],
#                     PDarray1_DataGroup[2].shape[0],PDarray1_DataGroup[3].shape[0]])
#
#all_data_summary=np.zeros((row_num_temp*4,32))
#all_data_summary[0:row_num_temp,:]=data_alternate(PDarray1_DataGroup[0],PDarray2_DataGroup[3],
#                                                  PDarray3_DataGroup[2],PDarray4_DataGroup[1])
#
#all_data_summary[row_num_temp:row_num_temp*2,:]=data_alternate(PDarray1_DataGroup[1],PDarray2_DataGroup[0],
#                                                               PDarray3_DataGroup[3],PDarray4_DataGroup[2])
#
#all_data_summary[row_num_temp*2:row_num_temp*3,:]=data_alternate(PDarray1_DataGroup[2],PDarray2_DataGroup[1],
#                                                                 PDarray3_DataGroup[0],PDarray4_DataGroup[3])
#
#all_data_summary[row_num_temp*3:row_num_temp*4,:]=data_alternate(PDarray1_DataGroup[3],PDarray2_DataGroup[2],
#                                                                 PDarray3_DataGroup[1],PDarray4_DataGroup[0])

#return all_data_summary

#test code
#def fft_draw(data_in):
#    
#    fig=plt.figure()    
#    data_lengh=len(data_in)
#    x=np.arange(data_lengh)
#    yy=fft(data_in)               #���ٸ���Ҷ�任   
#    yf=abs(yy)                 # ȡģ    
#   
#    #ԭʼ����
#    plt.subplot(211)
#    plt.plot(x,data_in)
#    plt.title('Original wave')
#    #FFT��˫��Ƶ�ʷ�Χ��
#    plt.subplot(212)
#    plt.plot(x,yf,'r') #��ʾԭʼ�źŵ�FFTģֵ
#    plt.title('FFT(two sides frequency range)',fontsize=7,color='#7A378B')  #ע���������ɫ���Բ�ѯ��ɫ�����
#    plt.show()
#
##
#plt.subplot(411)
#plt.plot(PDarrayA_DataGroup)
#plt.subplot(412)
#plt.plot(PDarrayB_DataGroup_rolled)
#plt.subplot(413)
#plt.plot(PDarrayC_DataGroup_rolled)
#plt.subplot(414)
#plt.plot(PDarrayD_DataGroup_rolled)
#plt.tight_layout()
#plt.draw()
##����Ƶ��Ϊ1000hz,�źű�������Ƶ��Ϊ500hz��Ҫ�˳�10hz����Ƶ�ʳɷ֣�������Ƶ��Ϊ10hz����wn=2*10/1000=0.02
#def lowpass_filter(data_in):
#    b, a = signal.butter(8, 0.02, 'lowpass')  
#    return signal.filtfilt(b, a, data_in)       #dataΪҪ���˵��ź�
    
#filted_data=lowpass_filter(PDarrayB_DataGroup[:,3])    
#fft_draw(filted_data)

