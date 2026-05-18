import pandas as pd
import numpy as np

# Pandas Dataframe is a data structure used for storing and manipulation data in table format(rows and columns).

# Creating empty Data frame:
df = pd.DataFrame([])
print(df)

print('-------------------------')

# Creating DataFrame using List

list = ['a','b','c','d','e','f']
df = pd.DataFrame(list)
print(df)

print('-------------------')

# Creating DataFrame using dict and  Numpy(py lib used to perform math operations faster.) array:

# data = {
#     'arr1' : np.array([1,2,3]),      
#     'arr2' : np.array([5,6,7]),
#     'arr3' : np.array([7,8,9])
# }

data = [
    {'name': 'Mike', 'degree': 'MBA', 'score': 90},
    {'name': 'Dan', 'degree': 'BCA', 'score': 40},
    {'name': 'Emilia', 'degree': 'M.Tech', 'score': 80},
]

df = pd.DataFrame(data)
print(df)