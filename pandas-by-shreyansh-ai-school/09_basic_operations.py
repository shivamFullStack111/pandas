import pandas as pd 

df = pd.DataFrame({
    "product_id": [101, 102, 103, 104],
    "product_name": ["Laptop", "Phone", "Tablet", "Camera"],
    "price": [60000, 30000, 25000, 45000],
    "cost":[3,6,3,4]
})
# =================================== APPLY FUNCTION ==================================================================
def square(n):
    return n**n

df["square"]=df["cost"].apply(square)          # apply() take a another function which send value of column one by one
print(df)

