# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:48:28 2019

@author: abc47
"""
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt 
from scipy.stats import norm
import myDP
import tkinter as tk
from tkinter import filedialog

load_data=myDP.Load_Save.Load_files(initialdir=os.getcwd()+'/')

        