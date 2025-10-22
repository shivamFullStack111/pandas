# In this file we are inserting new column in data frame

import pandas as pd

data={
    "name":["Shivam","Abhishek","Rohit","Rahul","Ramesh"],
    "company":"Google",
    "salary":[10000,20000,30000,40000,50000]
}

df = pd.DataFrame(data)

# Directly inserting column bonus using assignment operator 
df["bonus"] = df["salary"] * 0.10
print(df)

# Inserting column salary after bonus using insert function (industry standard)
df.insert(1,"bonusSalary",df["salary"]+df["bonus"])
print(df)
