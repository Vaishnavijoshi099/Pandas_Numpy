import pandas as pd

# numbers = [[x,x**2,x**3] for x in range(1,6)]

numbers = [[x, "Even" if x % 2 == 0 else "Odd"]
           for x in range(1,11)]

df = pd.DataFrame(numbers,columns=["Numbers","type"])

print(df)