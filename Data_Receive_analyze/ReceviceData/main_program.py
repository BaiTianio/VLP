import numpy as np

from GetData_From_Wifi     import get_wifi_data
#from ArrangeData           import data_arrange
#from DataInterpolate_Draw  import d2Cubic_interpol,draw_3d
#from Positioning           import find_Extreme,FindAll_ExtremePoint
#import time
#import os





Pos_length=200
Pos_angle=30
for times in range(3):
    raw_data=get_wifi_data() 
    save_path="../DataStroge/2020_1_13/({},{})_{}.npy".format(Pos_length,Pos_angle,times)
    print(save_path)
    np.save(save_path,raw_data)




#获取数据
#i=0
#while(i<20):
#    raw_data=get_wifi_data()
#    np.save(os.getcwd()+"\\raw_data\\data_%d.npy"%i,raw_data)
#    i=i+1
#    print("第%d次接收完成"%i)
#    time.sleep(10)
#raw_data=np.load(os.getcwd()+"\\raw_data\\data_%d.npy"%4)

#load_path=r"C:\Users\abc47\Desktop\VLP\RotateVLP\data\\"

#arranged_data=np.load(load_path+"data_44_1.npy")


#arranged_data=data_arrange(raw_data)
#draw_3d(arranged_data)
#d2Cubic_interpol_data=d2Cubic_interpol(arranged_data)
#draw_3d(d2Cubic_interpol_data)
#
#FindAll_ExtremePoint(d2Cubic_interpol_data)

#finded_data,max_index=find_Extreme(d2Cubic_interpol_data)
#draw_3d(finded_data)
#np.save("raw_data.npy",d2Cubic_interpol_data)
#np.savetxt("raw_data.csv",d2Cubic_interpol_data)
#d1Linear_interpol_data=d1Linear_interpol(formed_data)
#d2Cubic_interpol_data=d2Cubic_interpol(formed_data)
#draw_3d(d2Cubic_interpol_data)
#final_data=find_Extreme(d2Cubic_interpol_data)
#draw_3d(final_data)