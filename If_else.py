# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:49:52 2019

@author: feche
"""

N = int(input("Insert a number"))
if (N%2)!=0:
    print("Weird")
else:
    if (N>5) and (N<21):
        print("Weird")
    else:
        print("Not Weird")
        