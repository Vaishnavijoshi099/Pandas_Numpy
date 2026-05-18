import pandas as pd
import numpy as np

# Pandas series is a one dimensional array used to hold any time of data which is stored in SQL, a CSV file or a Excel file.

s = pd.Series()
print("Pandas Series: ", s)
data = np.array(['a','b','c','d','e'])

s = pd.Series(data)
print("Pandas Series:", s)


print('---------------------------------------------')


data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])

print(ser[22]) 


print('--------------------------------------------')

#Indexing a Series using .iloc[]

df_csv = pd.read_csv("dummy_data_1mb.csv")
series = pd.Series(df_csv["ARPDELDATE"])
data = series.head(4)

print(data.iloc[1:3])
