"""Create a Series of names: ["Ravi", "Anu", "Kiran", "John"]"""

import pandas as pd
import numpy as np

data = ["Ravi", "Anu", "Kiran", "John"]

series = pd.Series(data)

print(series)