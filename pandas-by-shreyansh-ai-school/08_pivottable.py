# =============================== PIVOT TABLE EXAMPLE ======================================================
# pivot_table() function is used to **create a custom summary table**
# It is often used for **analyzing data quickly** or preparing for heatmaps
# You can perform **aggregate functions** like mean, sum, min, max, count, etc.

import pandas as pd

data = {
    "store": ["A", "B", "A", "B", "C", "C"],
    "product": ["Laptop", "Mobile", "Laptop", "Mobile", "Laptop", "Mobile"],
    "sales": [50000, 30000, 55000, 28000, 48000, 35000],
    "quantity": [5, 8, 6, 7, 4, 9]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n")
print(df)
print("\n\n")




# =============================== SIMPLE PIVOT TABLE ======================================================
print("PIVOT TABLE - Average sales per store and product --------------------------------------------\n")

# index = rows (store)
# columns = columns (product)
# values = numeric column to aggregate (sales)
# aggfunc = aggregation function (mean = average)

pivot1 = df.pivot_table(index="store", columns="product", values="sales", aggfunc="mean")
print(pivot1)
print("\n")

#  Meaning:
# - Store A → Laptop average sales = (50000+55000)/2 = 52500
# - Store B → Mobile average sales = (30000+28000)/2 = 29000
# - Store C → Laptop = 48000, Mobile = 35000
# - NaN = no data for that product in that store








# =============================== PIVOT TABLE WITH MULTIPLE VALUES =========================================
print("PIVOT TABLE - Average sales and quantity per store and product --------------------------------\n")

# Now we can see both sales and quantity together in the same table
pivot2 = df.pivot_table(index="store", columns="product", values=["sales","quantity"], aggfunc="sum")   # We can provide any aggregate function like mean, max, min, sum
print(pivot2)
print("\n")


#  Meaning:
# - Store A → Laptop avg sales = 52500, avg quantity = 5.5
# - Store B → Mobile avg sales = 29000, avg quantity = 7.5
# - Store C → both Laptop and Mobile shown
# - NaN = no data for that product in that store

# =============================== NOTES ===============================================================
#  index → determines the rows of the pivot table
#  columns → determines the columns of the pivot table
#  values → numeric column to calculate
#  aggfunc → which aggregation to apply (mean, sum, min, max, count, etc.)
#  NaN → no data available for that combination
