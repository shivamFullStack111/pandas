import pandas as pd


data={
    "name":["Shivam","Abhishek","Rohit","Rahul","Ramesh"],
    "company":"Google",
    "salary":[10000,20000,30000,40000,50000],
    "city":'jalandhar'
}

df = pd.DataFrame(data)

df.drop(columns=["company","city"],inplace=True)       # inplace=True will delete original dataFrame
print(df)