import pandas as pd

# Selecting Columns:

df = pd.read_csv("fake_data.csv")

print(df[['Name','City']])

print('----------------------------------------------')

df['Experience'] = 1
print(df.head())

print('--------------------------------------------')

df.drop('Experience', axis=1,inplace=True)
print(df.head())

print('--------------------------------------------')

data = pd.read_csv("nba.csv", index_col="Team")

rows = data.loc["Utah Jazz"]

print(rows)

print("----------- Extracting rows between two indexes ----------------------------" )

data_new = pd.read_csv("nba.csv", index_col="Name")

rows_new = data_new.loc["Avery Bradley": "Amir Johnson"]

print(rows_new)

