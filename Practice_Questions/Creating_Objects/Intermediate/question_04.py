import pandas as pd
import numpy as np

data = {
    'ID': [1, 2, np.nan, 4],            
    'Name': ['Alice', np.nan, 'Charlie', 'Delta'], 
    'Status': [100, 'Pending', np.nan, 200]        
}

df = pd.DataFrame(data)

print(df)
