#!/usr/bin/python3
import numpy as np

a = np.arange(0, 1.1, 0.1, dtype=float) # (a) float from 0.0 to 1.0 step 0.1, shape=(11,),
print(a)
print(a.shape)

y = np.zeros( (5, 6), dtype=int ) # int zeros (1 byte) with shape=(5,6),
print(y)
print(y.shape) 

c = np.arange(1, 10, dtype=complex).reshape(9) * np.arange(9)# (c) complex with shape=(9,), powers of x = complex(0, 1): 1, x, x**2, ..., x**8.
print(c)
print(c.shape)
input()