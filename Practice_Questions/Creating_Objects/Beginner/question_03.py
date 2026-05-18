"""Create a Series with custom index: a → 100
b → 200
c → 300"""

import pandas as pd
import numpy as np

data = np.array(["a","b","c"])

index_series = pd.Series(data,index=[100,200,300])
print(index_series)