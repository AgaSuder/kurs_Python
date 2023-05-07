#!/usr/bin/python3
import numpy as np

m1 = np.arange(20).reshape((4,5)) # (a) Create a two dimensional array called m1, shape=(4,5).
print(m1)
m2 = m1[:,::-1]                   # (b) Create a new array m2 from m1, in which the elements of each row are in reverse order.
print(m2)
m3 = m1[::-1,:]                   # (c) Create a new array m3 from m1, in which the elements of each column are in reverse order.
print(m3)
m4 = m1[1:3,1:4]                  # (d) Cut of the first and last row and the first and last column of m1.
print(m4)
input()