import pandas as pd 

data = {
    "age": [22,34,54,45,63],
    "salary":[25000,45000,32000,60000,65000]
}


df = pd.DataFrame(data)

#  Single columns sort  
print(
    df.sort_values(by=["age"],ascending=True,inplace=False)              
)

print("\n")

#  Multiple columns sort  
print(
    df.sort_values(by=["age","salary"],ascending=[True,False],inplace=False)              
)