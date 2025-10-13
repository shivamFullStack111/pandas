import pandas as pd
data={
    "name":["Shivam","Abhishek","Rohit","Rahul",None],
    "company":["Google","TCS",None,"HCL","Microsoft"],
    "salary":[10000,None,30000,40000,50000]
}

df = pd.DataFrame(data)

print(df.isnull())        # Return True were null values exist and return False were null value does'nt exist 