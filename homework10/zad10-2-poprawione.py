#!/usr/bin/python3
import pandas as pd
import numpy as np
np.random.seed(0)
data = pd.date_range('20230501','20230531', freq ='D')
temperatures = np.random.randint(40, size=31)
ser = pd.Series(temperatures, data)
print(ser)
input()