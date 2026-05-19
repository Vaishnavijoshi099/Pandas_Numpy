import pandas as pd

data = {
    "Population":[70, 80, 100, 120]
}

index = [
    ("India", "Karnataka"),
    ("India", "Tamil Nadu"),
    ("USA", "Texas"),
    ("USA", "California")
]

multi_index = pd.MultiIndex.from_tuples(index)

df = pd.DataFrame(data,index=multi_index)

print(df)

