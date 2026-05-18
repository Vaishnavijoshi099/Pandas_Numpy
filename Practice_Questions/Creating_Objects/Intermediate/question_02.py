import pandas as pd

users = [
    {"id": 1, "name": "Alice", "role": "Admin"},
    {"id": 2, "name": "Bob", "role": "User"},
    {"id": 3, "name": "Charlie", "role": "User"}
]

df = pd.DataFrame(users,index=['row1','row2','row3'])

print(df)