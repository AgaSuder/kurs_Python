#!/usr/bin/python3
import pandas as pd
import numpy as np
# initialize list of lists
data = [['Hydrogen','H', 1], ['Helium','He', 4], ['Lithium','Li', 7],['Beryllium','Be', 9], ['Boron','B', 11], ['Carbon','C', 12], ['Nitrogen','N', 14], ['Oxygen','O', 16], ['Fluorine','F', 19], ['Neon','Ne', 20]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Symbol','Weight'])
df.index +=1 
# print dataframe.
print(df)
input()