import pandas as pd

df = pd.read_csv("Students_100records.csv")

"""Select Name"""
print(df["Name"])

"""Select Name and City"""
print(df[['Name','City']])

"""First 5 rows"""
print(df[1:5])

"""rows 2 to 8"""
print(df[2:8])

"""row label 3"""
print('-------------- row label 3 ----------')
print(df.loc[3])

"""3rd row"""
print('-------------- 3rd row --------------')
print(df.iloc[3])

"""first row and first column"""
print('---------------- first row and first column -----------------')
print(df.iloc[0,0])

"""last 3 rows"""
print('------------ last 3 rows -------------')
print(df.iloc[-3:])

""" rows 1 to 5 and columns 2 to 4"""
print('------------- rows 1 to 5 and columns 2 to 4 ------------')
print(df.iloc[1:5,2:4])

"""Age > 20"""
print('------ Age > 20 -----------')
print(df[df['Age']>20])