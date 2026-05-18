"""Create a DataFrame from list of lists:[
["Pen", 10],
["Book", 50],
["Bag", 500]
]"""

import pandas as pd

data = [
    ["Pen",10],
    ["Book",50],
    ["Bag",500]
]

df = pd.DataFrame(data,columns=['Products','Price'])
print(df)