import pandas as pd

df = pd.read_csv('nba.csv')

"""Salary > 500000"""
print('----------- Salary > 500000 ------------')
print(df[df['Salary']>5000000])

"""Team == New York Knicks"""
print('------------- Team == New York Knicks --------------')
print(df[df['Team']== "New York Knicks"])


df_new = pd.read_csv("Students_100records.csv")

"""Age > 20 AND Marks > 90"""
print("-------------- Age > 20 AND Marks > 90----------------------")
print(df_new[(df_new['Age'] > 20) & (df_new['Marks'] > 90)])

"""City == "Bangalore" OR Marks > 80"""
print('------------ City == "Bangalore" OR Marks > 80 ----------------')
print(df_new[(df_new['City']== "Banglore") | (df_new['Marks']>80)])

"""Marks between 70 and 90"""
print('----------- Marks between 70 and 90 -----------')
print(df_new[(df_new['Marks']>= 70) & (df_new['Marks']<=90)])