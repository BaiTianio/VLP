# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:25:48 2019

@author: abc47
"""
import numpy as np
#import matplotlib.pyplot as plt
#from scipy.fftpack import fft,ifft
#from scipy import signal

#Êý¾ÝÕûÀíº¯Êý
#data_in=np.load("raw_data.npy")

def data_arrange_1(data_in):
        
    #Ñ°ÕÒÊý¾ÝµÄÖ¡Í·
    for i in range(len(data_in)-27):
        if( data_in[i]==0     and data_in[i+9]==1  and 
            data_in[i+18]==2  and data_in[i+27]==3 ):
            data_in=data_in[i:]
            row_num=len(data_in)%9#±£Ö¤ÏòÁ¿¿ÉÒÔÅÅ³ÉnÐÐ9ÁÐµÄÐÎÊ½
            find_data=data_in[0:len(data_in)-row_num]
            data_storge=find_data.reshape(int(len(find_data)/9),9)
            break
     
     #¼ì²éÖ¡Í·¾ÝÖÐÊÇ·ñ»á³öÏÖ´íÎó   
    for x in data_storge[:,0]:
        if(x>7):
            raise Exception("arrange error")
     
    ##---------------Êý¾ÝÏà¼ÓµÃµ½×îÖÕÊýÖµ---------------------------   
    calculate_data=np.c_[data_storge[:,0],data_storge[:,1]*256+data_storge[:,2]]
    calculate_data=np.c_[calculate_data,data_storge[:,3]*256+data_storge[:,4]]
    calculate_data=np.c_[calculate_data,data_storge[:,5]*256+data_storge[:,6]]
    calculate_data=np.c_[calculate_data,data_storge[:,7]*256+data_storge[:,8]]
    return calculate_data    
        #    np.save("raw_data.npy",calculate_data)
def data_arrange_2(data_in):    
    #È·¶¨ÍêÕûµÄÖ¡Êý£¬½«ËùÓÐÊý¾ÝÖÐÃ¿¸öPDµÄÊý¾Ý³éÈ¡³öÀ´£¬½«Ò»×éPDµÄÊý¾Ý±£´æÎªÒ»¸ögroup²¢·µ»Ø
    def data_divide_group(data_in,group_num):  
        row_num=int(data_in.shape[0]/8)
        PDarray_data=np.zeros((row_num,8))
        #½«ËùÓÐÊý¾Ý°´ÕÕPDÕóÁÐ½øÐÐ·Ö×é
        for i in range(row_num):  
            if(data_in[i*8,0]==0 and data_in[i*8+7,0]==7):
                PDarray_data[i,:]=data_in[i*8:(i+1)*8,group_num].T  
                
        PDarrayGroup_data=np.c_[PDarray_data[:,0],PDarray_data[:,1],PDarray_data[:,2],PDarray_data[:,3],
                                PDarray_data[:,4],PDarray_data[:,5],PDarray_data[:,6],PDarray_data[:,7]]
        return PDarrayGroup_data
    
    #ÕýÈ·½Ç¶ÈÅÅÁÐÓ¦ÎªCBAD£¨3214£© 
    PDarrayA_DataGroup=data_divide_group(calculate_data,3)#ÆðÊ¼Î»ÖÃ0
    PDarrayB_DataGroup=data_divide_group(calculate_data,2)#ÆðÊ¼Î»ÖÃ-1/4
    PDarrayC_DataGroup=data_divide_group(calculate_data,1)#ÆðÊ¼Î»ÖÃ-2/4
    PDarrayD_DataGroup=data_divide_group(calculate_data,4)#ÆðÊ¼Î»ÖÃ-3/4
    
    PDarrayB_DataGroup=np.roll(PDarrayB_DataGroup,int(PDarrayB_DataGroup.shape[0]*3/4),axis=0)#½«B×éÊý¾ÝÑ­»·ÓÒÒÆ3/4,Ïàµ±ÓÚÑ­»·×óÒÆ1/4
    PDarrayC_DataGroup=np.roll(PDarrayC_DataGroup,int(PDarrayC_DataGroup.shape[0]*2/4),axis=0)#½«C×éÊý¾ÝÑ­»·ÓÒÒÆ2/4£¬Ïàµ±ÓÚÑ­»·×óÒÆ2/4
    PDarrayD_DataGroup=np.roll(PDarrayD_DataGroup,int(PDarrayD_DataGroup.shape[0]*1/4),axis=0)#½«C×éÊý¾ÝÑ­»·ÓÒÒÆ1/4£¬Ïàµ±ÓÚÑ­»·×óÒÆ3/4
    
    
    #Êý¾Ý´©²åÕûºÏ
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
##Êý×é³¤¶ÈµÄÎÊÌâ£¬ÔÚ·Ö¸îÊ±¿ÉÄÜ²úÉú²»µÈ³¤µÄ·Ö¸ô¶Î£¬Òò´ËÈ¡ËùÓÐ·Ö¸ô¶ÎµÄ×îÐ¡³¤¶È     
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
#    yy=fft(data_in)               #¿ìËÙ¸µÀïÒ¶±ä»»   
#    yf=abs(yy)                 # È¡Ä£    
#   
#    #Ô­Ê¼²¨ÐÎ
#    plt.subplot(211)
#    plt.plot(x,data_in)
#    plt.title('Original wave')
#    #FFT£¨Ë«±ßÆµÂÊ·¶Î§£©
#    plt.subplot(212)
#    plt.plot(x,yf,'r') #ÏÔÊ¾Ô­Ê¼ÐÅºÅµÄFFTÄ£Öµ
#    plt.title('FFT(two sides frequency range)',fontsize=7,color='#7A378B')  #×¢ÒâÕâÀïµÄÑÕÉ«¿ÉÒÔ²éÑ¯ÑÕÉ«´úÂë±í
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
##²ÉÑùÆµÂÊÎª1000hz,ÐÅºÅ±¾Éí×î´óµÄÆµÂÊÎª500hz£¬ÒªÂË³ý10hzÒÔÉÏÆµÂÊ³É·Ö£¬¼´½ØÖÁÆµÂÊÎª10hz£¬Ôòwn=2*10/1000=0.02
#def lowpass_filter(data_in):
#    b, a = signal.butter(8, 0.02, 'lowpass')  
#    return signal.filtfilt(b, a, data_in)       #dataÎªÒª¹ýÂËµÄÐÅºÅ
    
#filted_data=lowpass_filter(PDarrayB_DataGroup[:,3])    
#fft_draw(filted_data)

