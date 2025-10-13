# joining or merging 

import pandas as pd

# Create first DataFrame
data1 = {
    'id': [1, 2, 3, 4],
    'name': ['Amit', 'Ravi', 'Priya', 'Kiran']
}
df1 = pd.DataFrame(data1)

# Create second DataFrame
data2 = {
    'id': [3, 4, 5, 6],
    'city': ['Delhi', 'Mumbai', 'Pune', 'Chennai']
}
df2 = pd.DataFrame(data2)

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# 🔹 INNER JOIN – returns only matching rows from both DataFrames
inner_join = pd.merge(df1, df2, on='id', how='inner')
print("\nINNER JOIN:\n", inner_join)

# 🔹 LEFT JOIN – returns all rows from left DataFrame + matching rows from right
left_join = pd.merge(df1, df2, on='id', how='left')
print("\nLEFT JOIN:\n", left_join)

# 🔹 RIGHT JOIN – returns all rows from right DataFrame + matching rows from left
right_join = pd.merge(df1, df2, on='id', how='right')
print("\nRIGHT JOIN:\n", right_join)

# 🔹 OUTER JOIN – returns all rows from both DataFrames (matches + non-matches)
outer_join = pd.merge(df1, df2, on='id', how='outer')
print("\nOUTER JOIN:\n", outer_join)

# 🔹 CROSS JOIN – returns every possible combination of rows from both DataFrames
cross_join = pd.merge(df1, df2, how='cross')
print("\nCROSS JOIN:\n", cross_join)
