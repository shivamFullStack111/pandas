import pandas as pd

# Create first DataFrame
data1 = {
    'id': [1, 2, 3],
    'name': ['Amit', 'Ravi', 'Priya']
}
df1 = pd.DataFrame(data1)

# Create second DataFrame
data2 = {
    'id': [4, 5, 6],
    'name': ['Kiran', 'Neha', 'Suresh']
}
df2 = pd.DataFrame(data2)

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# 🔹 1. Row-wise concatenation (one below another, like UNION ALL)
concat_rows = pd.concat([df1, df2])
print("\nRow-wise Concatenation:\n", concat_rows)

# 🔹 2. Row-wise with new index (ignore old index numbers)
concat_rows_reset = pd.concat([df1, df2], ignore_index=True)
print("\nRow-wise Concatenation with Reset Index:\n", concat_rows_reset)

# 🔹 3. Column-wise concatenation (side by side, like JOIN on index)
concat_columns = pd.concat([df1, df2], axis=1)
print("\nColumn-wise Concatenation:\n", concat_columns)

# 🔹 4. Concatenation with keys (multi-level index to identify source)
concat_with_keys = pd.concat([df1, df2], keys=['Batch1', 'Batch2'])
print("\nConcatenation with Keys (MultiIndex):\n", concat_with_keys)
