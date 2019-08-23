# coding:utf-8
import numpy as np
from socket import *
#from func_timeout import func_set_timeout

#@func_set_timeout()
def get_wifi_data():
    #    print("=====================TCP服务器=====================")
    HOST = '192.168.1.104'  #主机号为空白表示可以使用任何可用的地址。
    PORT = 8080  #端口号
    BUFSIZ = 2048  #接收数据缓冲大小
    ADDR = (HOST, PORT)
    tcpSerSock = socket(AF_INET, SOCK_STREAM) #创建TCP服务器套接字
    tcpSerSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    tcpSerSock.bind(ADDR)  #套接字与地址绑定
    tcpSerSock.listen(1) #监听连接，同时连接请求的最大数目
    
    receive_flag=0
    stroge_data=0
    
    try:
        print('等待客户端的连接...')
        tcpCliSock, addr = tcpSerSock.accept()
        #接收客户端连接请求
        print('取得连接:', addr)
        F_num=0
        valid_F_num=0
        raw_data=np.zeros(2050)
        #数据接收
        while F_num<500:
            wifi_data = tcpCliSock.recv(BUFSIZ)  #连续接收指定字节的数据，接收到的是字节数组
            rece_index=0
            for x in wifi_data:
                raw_data[rece_index]=x
                rece_index+=1
            raw_data_cache=raw_data[0:rece_index]    
            
            #接收控制
            sign_point=np.where(raw_data==255)[0]
            for i in range(len(sign_point)):
                if(sign_point[i]-sign_point[i-1]==1):#检测到两个连续的255
                    receive_flag+=1
                    if(receive_flag==1):
                        raw_data_cache=raw_data_cache[sign_point[i]+1:]#保留好的数据
                    elif(receive_flag==2):
                        raw_data_cache=raw_data_cache[:sign_point[i]-1]
             
            #数据保存
            if(receive_flag!=0):
                stroge_data=np.append(stroge_data,raw_data_cache)
                valid_F_num+=1
                print(valid_F_num)
            if(receive_flag>=2):
                if(valid_F_num>5):
                    return stroge_data
                else:
                    stroge_data=0
                    receive_flag=0
                    valid_F_num=0
            F_num+=1        
#            if __name__ == '__main__':
            print(valid_F_num)
    finally:
        tcpCliSock.close()  #关闭与客户端的连接
        tcpSerSock.close()  #关闭服务器socket
#  np.save("raw_data.npy",raw_data)
