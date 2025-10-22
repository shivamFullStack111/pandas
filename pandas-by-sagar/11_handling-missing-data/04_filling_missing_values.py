import pandas as pd

data={
    "name":["Shivam","Abhishek","Rohit","Rahul",None],
    "company":["Google","TCS","Infosys","HCL","Microsoft"],
    "salary":[10000,None,30000,40000,50000]
}

df = pd.DataFrame(data)

# Replacing null value with Static value---------------------------------------------------------------------
dataAfterFillingNullValues = df.fillna(111,inplace=False)   # All null value replace with 111 and inplace=False does'nt change original data set
print(dataAfterFillingNullValues)

print("\n")                             

# Replacing with mean of columns
df["salary"].fillna(df["salary"].mean(),inplace=True)       # replace null value of salary with average of salary and inplace=True change original value
print(df)


