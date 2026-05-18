````md
# NumPy and Pandas - Complete Beginner Guide

## Table of Contents

1. Introduction
2. Installation
3. NumPy
   - What is NumPy?
   - Creating Arrays
   - Array Properties
   - Indexing and Slicing
   - Reshaping Arrays
   - Mathematical Operations
   - Statistical Functions
   - Broadcasting
   - Random Module
   - Linear Algebra
4. Pandas
   - What is Pandas?
   - Series
   - DataFrame
   - Creating Objects
   - Viewing Data
   - Selecting and Slicing
   - Filtering Data
   - Handling Missing Values
   - Sorting
   - GroupBy
   - Merge and Join
   - Date & Time Handling
   - File Handling
5. Practice Questions
6. Interview Questions
7. Best Practices
8. Learning Resources

---

# 1. Introduction

## What is NumPy?

NumPy (Numerical Python) is a Python library used for:

- Fast mathematical operations
- Multi-dimensional arrays
- Matrix operations
- Linear algebra
- Statistical calculations

### Why NumPy?

- Faster than Python lists
- Consumes less memory
- Supports vectorized operations

---

## What is Pandas?

Pandas is a Python library used for:

- Data analysis
- Data cleaning
- Data manipulation
- Working with CSV, Excel, JSON files
- Data visualization preparation

### Why Pandas?

- Easy data handling
- Powerful filtering
- Works with structured data
- Supports missing values handling

---

# 2. Installation

Install NumPy and Pandas:

```bash
pip install numpy pandas
````

Import libraries:

```python
import numpy as np
import pandas as pd
```

Check version:

```python
print(np.__version__)
print(pd.__version__)
```

---

# 3. NumPy

## 3.1 Creating Arrays

### 1D Array

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
```

### 2D Array

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)
```

### Special Arrays

#### Zeros

```python
arr = np.zeros((2, 3))
print(arr)
```

#### Ones

```python
arr = np.ones((2, 2))
print(arr)
```

#### Identity Matrix

```python
arr = np.eye(3)
print(arr)
```

#### Range

```python
arr = np.arange(1, 10)

print(arr)
```

#### Evenly Spaced Numbers

```python
arr = np.linspace(1, 10, 5)

print(arr)
```

---

## 3.2 Array Properties

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(arr.size)
```

### Important Properties

| Property | Meaning              |
| -------- | -------------------- |
| shape    | Rows and columns     |
| ndim     | Number of dimensions |
| dtype    | Data type            |
| size     | Total elements       |

---

## 3.3 Indexing and Slicing

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[-1])
```

### Slicing

```python
print(arr[1:4])
print(arr[:3])
print(arr[::2])
```

### 2D Indexing

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr[0, 1])
print(arr[:, 1])
```

---

## 3.4 Reshaping Arrays

```python
arr = np.arange(12)

new_arr = arr.reshape(3, 4)

print(new_arr)
```

Flatten Array

```python
print(new_arr.flatten())
```

---

## 3.5 Mathematical Operations

```python
arr = np.array([1, 2, 3, 4])

print(arr + 10)
print(arr * 2)
print(arr ** 2)
```

Array Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)
```

---

## 3.6 Statistical Functions

```python
arr = np.array([10, 20, 30, 40])

print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.max(arr))
print(np.min(arr))
```

---

## 3.7 Broadcasting

```python
arr = np.array([1, 2, 3])

print(arr + 5)
```

Output:

```python
[6 7 8]
```

---

## 3.8 Random Module

```python
print(np.random.rand(3))
```

Random Integers

```python
print(np.random.randint(1, 100, 5))
```

Random Matrix

```python
print(np.random.randn(3, 3))
```

---

## 3.9 Linear Algebra

Dot Product

```python
a = np.array([1, 2])
b = np.array([3, 4])

print(np.dot(a, b))
```

Matrix Multiplication

```python
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(np.matmul(a, b))
```

---

# 4. Pandas

## 4.1 Series

A Series is a one-dimensional labeled array.

```python
import pandas as pd

data = pd.Series([10, 20, 30])

print(data)
```

---

## 4.2 DataFrame

A DataFrame is a table with rows and columns.

```python
data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 28]
}

df = pd.DataFrame(data)

print(df)
```

---

## 4.3 Creating Objects

From Dictionary

```python
data = {
    "Name": ["A", "B"],
    "Marks": [90, 85]
}

df = pd.DataFrame(data)
```

From List

```python
data = [
    ["A", 90],
    ["B", 85]
]

df = pd.DataFrame(data,
                  columns=["Name", "Marks"])
```

---

## 4.4 Viewing Data

```python
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
```

---

## 4.5 Selecting and Slicing

Select Column

```python
print(df["Name"])
```

Multiple Columns

```python
print(df[["Name", "Marks"]])
```

Using loc

```python
print(df.loc[0])
```

Using iloc

```python
print(df.iloc[0:2])
```

---

## 4.6 Filtering Data

```python
print(df[df["Marks"] > 85])
```

Multiple Conditions

```python
print(
    df[
        (df["Marks"] > 80)
        & (df["Name"] == "A")
    ]
)
```

---

## 4.7 Handling Missing Values

Check Missing Values

```python
print(df.isnull())
```

Drop Missing Values

```python
df.dropna()
```

Fill Missing Values

```python
df.fillna(0)
```

---

## 4.8 Sorting

```python
df.sort_values(by="Marks")
```

Descending Order

```python
df.sort_values(
    by="Marks",
    ascending=False
)
```

---

## 4.9 GroupBy

```python
data = {
    "Department": [
        "IT",
        "IT",
        "HR"
    ],
    "Salary": [
        50000,
        60000,
        45000
    ]
}

df = pd.DataFrame(data)

print(
    df.groupby("Department")
    ["Salary"]
    .mean()
)
```

---

## 4.10 Merge and Join

```python
df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["A", "B"]
})

df2 = pd.DataFrame({
    "ID": [1, 2],
    "Marks": [90, 85]
})

merged = pd.merge(
    df1,
    df2,
    on="ID"
)

print(merged)
```

---

## 4.11 Date & Time Handling

```python
dates = pd.date_range(
    start="2025-01-01",
    periods=5
)

print(dates)
```

Convert String to Datetime

```python
df["Date"] = pd.to_datetime(
    df["Date"]
)
```

---

## 4.12 File Handling

Read CSV

```python
df = pd.read_csv("data.csv")
```

Save CSV

```python
df.to_csv(
    "output.csv",
    index=False
)
```

Read Excel

```python
df = pd.read_excel("data.xlsx")
```

Save Excel

```python
df.to_excel(
    "output.xlsx",
    index=False
)
```

---

# 5. Practice Questions

## NumPy

1. Create a NumPy array of numbers 1 to 50.
2. Find even numbers from array.
3. Reshape an array into 5x5 matrix.
4. Find mean, median and standard deviation.
5. Generate random numbers.

## Pandas

1. Create DataFrame of students.
2. Display first 5 rows.
3. Filter marks > 80.
4. Sort based on marks.
5. Find average marks.

---

# 6. Interview Questions

## NumPy Interview Questions

1. What is NumPy?
2. Difference between list and NumPy array?
3. What is broadcasting?
4. Difference between reshape() and flatten()?
5. Difference between arange() and linspace()?

## Pandas Interview Questions

1. What is Pandas?
2. Difference between Series and DataFrame?
3. Difference between loc and iloc?
4. Difference between merge and join?
5. How to handle missing values?

---

# 7. Best Practices

* Use vectorized operations.
* Avoid loops in NumPy.
* Use meaningful column names.
* Handle missing values properly.
* Use `loc` and `iloc` carefully.
* Keep data clean.

---

# 8. Learning Resources

Official Documentation:

* NumPy: [https://numpy.org/doc/](https://numpy.org/doc/)
* Pandas: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)

GitHub:

```bash
git init
git add .
git commit -m "Initial Commit"
```

Happy Learning 🚀

```
```
