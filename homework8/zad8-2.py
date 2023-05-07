#!/usr/bin/python3
import numpy as np

v1 = np.arange(10) # (a) Create an arbitrary one dimensional array called v1.
v2 = v1[1:len(v1):2] # (b) Create a new array v2 which consists of the odd indices of v1.
print(v2)
v3 = v1[::-1]       # (c) Create a new array v3 in backwards ordering from v1.
print(v3)
input()