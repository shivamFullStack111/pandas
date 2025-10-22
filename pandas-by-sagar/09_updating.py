# In this file i am updating value of specific row 

import pandas as pd

data={
    "name":["Shivam","Abhishek","Rohit","Rahul","Ramesh"],
    "company":"Google",
    "salary":[10000,20000,30000,40000,50000]
}

df = pd.DataFrame(data)

# Updating using loc property------------------------------------------------------------

updatedData = df.loc[1,"company"]="TCS"                            # 1 is row index and "company" is column name 
print(df)
print("\n")


# Directly updating column but in this we are changing value for all row-----------------

df['company'] = "Microsoft"                                        
print(df)