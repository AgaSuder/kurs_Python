#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import math
# Fixing random state for reproducibility
np.random.seed(19680801)
n = 100
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.where(np.sqrt((x*x + y*y)) > 1 ,'r', 'g')
area = (np.absolute(x)+np.absolute(y))
plt.scatter(x, y, s=area, c=colors)
plt.show()

input()