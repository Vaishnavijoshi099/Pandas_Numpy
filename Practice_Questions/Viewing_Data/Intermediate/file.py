import pandas as pd

df = pd.read_csv("Students_100records.csv")

"""top 10 rows"""
print(df.head(10))

"""bottom 7 rows"""
print(df.tail(7))

"""memory usage"""
print(df.memory_usage())

"""null values count"""
print(df.isnull().sum())

"""only numeric column summary"""
print(df.describe())

"""number of unique values"""
print(df['Age'].unique())

"""minimum and maximum salary"""
print(df['Marks'].max())
print(df['Marks'].min())

"""most frequent city"""
print('--------- most frequent city -----------')
print(df['City'].mode())

"""Check duplicate rows."""
print('-------------- Check duplicate rows ------------')
print(df['City'].duplicated())

