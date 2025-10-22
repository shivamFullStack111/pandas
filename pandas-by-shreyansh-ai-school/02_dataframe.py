# Combining a multiple serues become DataFrame but only single index/labels exist 
# DataFrame contain single index/labels and multiple columns/values
# We can also create DataFrame by list, dictionary.

import numpy as np
import pandas as pd



# ======================= CREATING DATAFRAME USING DICTIONARY =========================================================================

print("CREATING DATAFRAME USING DICTIONARY-----------------------------")

data={
    "name":["Shivam","Abhishek","Rohit","Rahul","Ramesh"],
    "company":"Google",
    "salary":[10000,20000,30000,40000,50000]
}

df1 = pd.DataFrame(data)
print(df1,"\n")








# ======================= CREATING DATAFRAME USING LIST ================================================================================

print("CREATING DATAFRAME USING LIST-----------------------------")

lst = [
    ["Joe","Google",10000],
    ["Jack","Google",80000],
    ["Baki","Google",30000],
    ["Youjiro","Google",70000],
    ["Hanayama","Google",30000],
]
cols = ["name","company","salary"]

# If we are not providing column names this will automatically create column names in number from 0 to n-1 
df2 = pd.DataFrame(lst,columns=cols)

print(df2,"\n")








# ================================= ACCESSING COLUMNS ====================================================================================

# If we access single column this will return Series with index/labels and values

print("ACCESSING COLUMNS FROM DATAFRAME-----------------------------")

print(df2.name)
print(df2["salary"])
print(df2[["company","name"]],"\n")








# ================================= ACCESSING ROWS ====================================================================================

print("ACCESSING ROWS FROM DATAFRAME-----------------------------")

print(
    df2.loc[2]                # Accessing 2nd index rows && this returns a series 
)

print(
    df2.loc[[4,2,1]]          # Accessing multiple rows
)

print("\n")






# ================================= ACCESSING ROWS AND COLUMNS SAME TIME ====================================================================================

print("ACCESSING ROWS AND COLUMNS SAME TIME-----------------------------")

data = df2.loc[[0,1]][["name","company"]]            # loc[<row-Index>][<column-name>] 
#                                                    # loc[[<row-indexes>]][[<column-names>]]          for multiple rows and columns
print(data)

print("\n")











# ================================= ACCESSING BY CONDITIONS ====================================================================================

print("ACCESSING BY CONDITIONS-----------------------------")

print(
    df2[df2["salary"]>30000]
)

print(
    df2[ (df2["salary"]>10000) & (df2["salary"]<40000) ]
)


print("\n")










# ====================================== CREATING/INSERTING COLUMNS ==========================================================================

print("INSERTING COLUMNS TO DATAFRAME-----------------------------")

# directly adding column 
newCol1 = ["project manager","full stack developer","devops engg.", "full stack developer","data scientist"]
df2["designation"] = newCol1
print(df2)

# adding column using insert method 
newCol2 = ["male","male","female","male","female"]
df2.insert(4,"gender",newCol2)
print(df2,"\n")









# ============================================ DROPING/DELETING COLUMN ==========================================================

print("DELETING COLUMNS FROM DATAFRAME-----------------------------")

df2.drop(4,axis=0,inplace=True)                       # axis=0 will delete 4th index row by default axis set on 0 which search on rows && inplace=True change original DataFrame
print(df2)

print(
    df2.drop("gender",axis=1)                         # axis=1 search on column means it will find column name gender and delete it
)                       

print(
    df2.drop(columns=["name","salary"],axis=1),        # Deleting multiple columns
)  
   
print("\n")

