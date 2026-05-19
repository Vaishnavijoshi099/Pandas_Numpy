import pandas as pd

names = ["John","Peter","Jenifer"]
ages = [23,34,43]
cities = ["Delhi","Mumbai","Banglore"]

data = list(zip(names,ages,cities))

df = pd.DataFrame(data,columns=["Name","Age","City"])

print(df)
