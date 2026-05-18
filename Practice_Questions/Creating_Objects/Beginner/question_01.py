"""Create a Pandas Series containing numbers: 10, 20, 30, 40, 50"""

import pandas as pd
import numpy as np

data = np.array([10,20,30,40,50])

series = pd.Series(data)
print(series)