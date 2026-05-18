import pandas as pd

students = {
    'student1': {'name': 'Alice', 'age': 20, 'grade': 'A'},
    'student2': {'name': 'Bob', 'age': 22, 'grade': 'B'}
}

df = pd.DataFrame(students)

print(df)