import pandas as pd

Category = ["Electronics","Electronics","Furniture","Furniture"]
Products = ["Laptop","Mobile","Chair","Table"]

data = {
    "Prices":[50000, 20000, 5000, 7000]
}

multi_index = pd.MultiIndex.from_arrays([Category,Products])

df = pd.DataFrame(data, index=multi_index)

print(df)
