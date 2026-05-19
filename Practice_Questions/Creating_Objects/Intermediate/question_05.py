"""Create a MultiIndex DataFrame."""

import pandas as pd

data = {
    "Marks": [86,78,90,67]
}

index = {
    ("Class A","Maths"),
    ("Class A","Science"),
    ("Class B","Maths"),
    ("Class B","Science")
}

multi_index = pd.MultiIndex.from_tuples(index)

df = pd.DataFrame(data,index=multi_index)

print(df)