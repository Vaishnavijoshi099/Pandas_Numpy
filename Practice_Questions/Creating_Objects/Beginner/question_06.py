"""Create a DataFrame using NumPy random values with:
5 rows
4 columns
column names:"""

import pandas as pd
import numpy as np

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]

data = np.array(matrix)

df = pd.DataFrame(data,columns=['A','B','C','D'], index=[102,103,104,105,106])

print(df)