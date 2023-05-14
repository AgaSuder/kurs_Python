#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)   # start,stop,step
sin = np.sin(x)

plt.plot(x,sin,'r-')

cos = np.cos(x)
plt.plot(x,cos, 'g.')
exp = np.exp(-x)
plt.plot(x,exp, 'b--')
plt.legend(['sin(x)','cos(x)', 'exp(-x)'])
plt.show()

input()