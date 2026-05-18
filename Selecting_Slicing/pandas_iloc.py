# Extracting rows using .iloc[]
""".iloc[] is an indexer used for integer-location-based indexing of data in a DataFrame.
It allows users to select specific rows and columns by providing integer indices, making it a valuable tool for data manipulation and extraction based on numerical positions within the DataFrame."""

import pandas as pd

data = pd.read_csv("nba.csv")

row_1 = data.loc[3]

row_2 = data.iloc[3]

print("----------Loc output -------------")
print(row_1)
print()
print("----------iloc output -------------")
print(row_2)


print("---------------- Examples -----------------")

row_3 = data.iloc[[4,5,6,7]]
print()
print("-----------------list based indexing --------------")
print(row_3)

print("----------------------------------------")

row_4 = data.iloc[3:9]   # [start,end-1]

print(row_4)