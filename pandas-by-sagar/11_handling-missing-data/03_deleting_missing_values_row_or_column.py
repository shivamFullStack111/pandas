import pandas as pd

data={
    "name":["Shivam","Abhishek","Rohit","Rahul",None],
    "company":["Google","TCS","Infosys","HCL","Microsoft"],
    "salary":[10000,None,30000,40000,50000]
}

df = pd.DataFrame(data)

dataAfterRemoveNullValues = df.dropna(axis=0)                # axis=0 remove complete row if the null exist 
                                                             # axis=1 remove complete column in if in column any value is null

# or we can drop row from specific columns 
removedNullForSpecificColumns=df.dropna(subset=['salary','company'])   # this will delete rows if the null value exist in these columns

                                                             
print(dataAfterRemoveNullValues)
