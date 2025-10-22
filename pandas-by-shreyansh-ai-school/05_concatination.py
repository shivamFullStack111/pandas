import pandas as pd

df1 = pd.DataFrame({
    "product_id": [101, 102, 103],
    "product_name": ["Laptop", "Phone", "Tablet"],
    "price": [60000, 30000, 25000]
})

df2 = pd.DataFrame({
    "product_id": [104, 105, 106],
    "product_name": ["Camera", "Smartwatch", "Headphones"],
    "price": [45000, 15000, 3000]
})

print(
    pd.concat([df1,df2]),         # Concatinating in rows by default axis=0
    "\n"
)
print(
    pd.concat([df1,df2],axis=1),  # Concatinating in columns this will create extra columns (duplicate columns name) 
    "\n"
)
