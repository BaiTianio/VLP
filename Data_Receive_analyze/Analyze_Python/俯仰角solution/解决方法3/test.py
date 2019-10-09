import time
N=int(input())
stroge={}
size=0
while(1):
    try:
        a,b=input().strip().split()
    except:exit() 
    b=int(b)
    if(a in stroge.keys()):
        if(stroge[a][0]<b):
            stroge_time=time.clock()
            stroge={}
            stroge[a]=[b,stroge_time]
    else:
        if(size<N):
#            print('here',N)
            stroge_time=time.clock()
            stroge={}
            stroge[a]=(b,stroge_time)
            size+=1
        else:
            min_value=list(stroge.values())[0][1]
            st_index=list(stroge.keys())[0]
            for index in stroge.keys():
                if(stroge[index][1]<min_value):
                    st_index=index
            stroge.pop(st_index)
            print(st_index+' '+str(stroge[st_index][1]))                    
#    except:exit()

