#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:34:37 2019

@author: bxt
"""

import numpy as np
from ArrangeData           import data_arrange_1,data_arrange_2
raw_data=np.load("./data_45_1.npy")
arranged_data_1=data_arrange_1(raw_data)