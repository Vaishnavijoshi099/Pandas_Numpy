"""Create a DataFrame using dictionary:Student_Name
Age
Marks"""

import pandas as pd

data = [
    {'Student_name':"Vaishnavi", "Age":23,"Marks":89},
    {'Student_name':"Samiksha", "Age":23,"Marks":90},
    {'Student_name':"Sneha", "Age":24,"Marks":95}
]

result = pd.DataFrame(data)

print(result)