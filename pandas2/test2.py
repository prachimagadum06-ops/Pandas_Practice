import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "age": [20, 22, 19, 25, 21],
    "city": ["Bangalore", "Mumbai", "Delhi", "Chennai", "Pune"],
    "salary": [30000, 45000, 25000, 60000, 40000]
}

df = pd.DataFrame(data)

print(df)

print(df.head(3))

print(df.tail(2))

print(df.columns)







