# In this file we are converting data to other extension files like .csv, .xlsx, .json etc...

import pandas as pd

data={
    "name":"Shivam",
    "class":"BCA",
    "subjects":["python","DWM","AWS","AI/ML"]
}

df = pd.DataFrame(data)

df.to_csv("files/data.csv",index=True) # This will create data.csv file 
df.to_excel("files/data.xlsx")
df.to_json("files/data.json")
df.to_html("files/data.html")

# etc...