# Merge: Combines DataFrames by matching column values.
# Join: Combines DataFrames by matching index (default).

import pandas as pd

df1 = pd.DataFrame({
    "name": ["Aarav", "Vihaan", "Kabir", "Rudra"],
    "age": [25, 28, 30, 27]
}, index=[101, 102, 103, 104])  # Custom index

df2 = pd.DataFrame({
    "department": ["IT", "Finance", "HR", "Marketing"],
    "salary": [60000, 75000, 50000, 72000]
}, index=[102, 103, 104, 105])  # Custom index



print(
    df1.join(df2,how="inner"),
    "\n"
)
print(
    df1.join(df2,how="outer"),
    "\n"
)
print(
    df1.join(df2,how="left"),
    "\n"
)
print(
    df1.join(df2,how="right"),
    "\n"
)