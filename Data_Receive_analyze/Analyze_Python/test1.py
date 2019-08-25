# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:16:54 2019

@author: abc47
"""


listTemp = range(1,10)
for i,s in enumerate(listTemp):
    locals()['a'+str(i)]=i
#print(a1,a2,a3)