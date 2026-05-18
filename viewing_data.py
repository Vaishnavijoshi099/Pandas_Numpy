import pandas as pd

data = pd.read_csv('dummy_data_1mb.csv')

# head() is used to fetch first 5 rows

print(data.head())

#can fetch rows from a specific column 
print('------------------------------')

file_name = data[['ARCVFILENAME','SERVNAME']].head()

print(file_name)

# tail() is used to fetch last 5 rows of the Dataframe/ Series

print('-----------------------------------')

print(data.tail(1))

# Using tail() on a Series

print('-----------------------------------')

archive_id = data['ARCHIVEID']

print(archive_id.tail(2))

print('----------------------------------------')
print('Summary table using .describe() method')

print(data.describe())

# describe() method also works with string data
print('--------------------------------------------')
str = data['GUID'].describe(include='all')

print(str)