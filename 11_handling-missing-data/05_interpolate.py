import pandas as pd

data={
    "name":["Shivam","Abhishek","Rohit","Rahul",None],
    "company":["Google","TCS","Infosys","HCL","Microsoft"],
    "salary":[10000,None,30000,40000,50000]
}

df = pd.DataFrame(data)

# Filling data with linear mathematical method that fill data in sequence manner like 10 20 30 NaN 50 NaN replace with 50
df["salary"].interpolate("linear",inplace=True)
print(df)