import pandas as pd

"""Create a student DataFrame and display:
first 5 rows"""

df = pd.read_csv("Students_100records.csv")
print(df.head())

"""Display: last 3 rows"""
print(df.tail(3))

"""Find: number of rows and columns"""
print(df.shape)

"""Print: column names only"""
print(df.columns)

"""Print: index values"""
print(df.index.values)

"""Check: datatype of each column"""
print(df.dtypes)

"""Get summary statistics."""
print(df.describe())

"""Display random 4 rows."""
print(df.sample(4))

"""Print complete information about DataFrame."""
print(df.info())

"""Count unique values in: Department"""
print(df['City'].unique())