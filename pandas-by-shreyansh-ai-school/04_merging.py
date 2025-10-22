# Merge: Combines DataFrames by matching column values.
# Join: Combines DataFrames by matching index (default).

import pandas as pd 
import numpy as np 


# Product details
df1 = pd.DataFrame({
    "product_id": [101, 102, 103, 104],
    "product_name": ["Laptop", "Phone", "Tablet", "Camera"],
    "price": [60000, 30000, 25000, 45000]
})

# Sales details
df2 = pd.DataFrame({
    "product_id": [103, 104, 105],
    "units_sold": [25, 30, 10],
    "revenue": [625000, 1350000, 300000]
})



print(
    pd.merge(df1,df2,how="inner",on="product_id"),        # Only rows that match in both tables..   
    "\n"
)
print(
    pd.merge(df1,df2,how="outer",on="product_id"),        # All rows from both tables, fill missing with NaN.
    "\n"
)
print(
    pd.merge(df1,df2,how="left",on="product_id"),         # All rows from left table + matching from right.
    "\n"
)
print(
    pd.merge(df1,df2,how="right",on="product_id"),        # All rows from right table + matching from left.  
    "\n"
)

print("\n")