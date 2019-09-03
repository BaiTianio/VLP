import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog

try:
    with open("./数据保存文件夹地址.txt",'r') as path_file:
        load_path=path_file.read()
        print(load_path)  
    FileList=list(filter(lambda x:(x[-4:]==".csv"),os.listdir(load_path)))
    for file in FileList:
        var_name=file[0:-4]
        globals()[var_name]=pd.read_csv(load_path+'/'+file)#加载测量数据
        
except(FileNotFoundError):
    root=tk.Tk()
    root.withdraw()
    newpath=filedialog.askdirectory()
    with open("./数据保存文件夹地址.txt",'w') as path_file:
        load_path=path_file.write(newpath)
