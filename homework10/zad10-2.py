#!/usr/bin/python3
import pandas as pd
import numpy as np
np.random.seed(0)
data = np.arange(1, 32)
temperatures = np.random.randint(40, size=31)
ser = pd.Series(data, temperatures)
print(ser)
input()