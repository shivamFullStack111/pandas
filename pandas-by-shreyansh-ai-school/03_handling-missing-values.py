import pandas as pd 
import matplotlib as plt

data = {
    "name": ["Aarav", "Vihaan", None, "Reyansh", "Ishaan", None, "Kabir", "Arjun", None, "Rudra", "Atharv", "Dev", "Manan", None, "Riyan", "Shaurya", "Vihaan", None, "Aarav", "Kabir"],
    "age": [25, None, 30, 28, 35, 53, 40, 31, None, 29, 33, 26, None, 38, 27, 32, 45, 53, 24, 36],
    "city": ["Delhi", "Mumbai", "Pune", "Punjab", "Kolkata", "Bangalore", None, "Hyderabad", "Delhi", None, "Pune", "Mumbai", None, "Chennai", "Kolkata", "Delhi", None, "Hyderabad", "Pune", "Bangalore"],
    "department": ["IT", "HR", "Finance", None, "Sales", "Marketing", "HR", None, "IT", "Finance", None, "Admin", "IT", "Sales", None, "Finance", "Marketing", "HR", None, "IT"],
    "salary": [50000, 60000, None, 55000, 70000, 65000, None, 72000, 48000, None, 51000, 58000, 60000, None, 75000, 68000, None, 54000, 71000, None]
}

df = pd.DataFrame(data)







# ================================== FINDING NULL VALUES ==========================================

print("FINDING NULL VALUES ------------------------------------------------")
 
print(df.isna())                 # Finding in whole DataFrame
print(df["age"].isna())          # Finding in particular DataFrame
print(df.isna().sum())           # print(df.isna().sum())   # This returns a Series showing the total number of null (NaN) values in each column
print(df.isna().any())           # This returns True in which column null value exist and False in which column null value does'nt exist
print("\n")








# ========================== REMOVING NULL VALUES =============================================

print("REMOVING NULL VALUES ------------------------------------------------")

print(
    df.dropna(),                   # This will remove all rows in which null values exist because by default axis=0 
)
print(
    df.dropna(axis=1)              # Removing all columns in which null values exist 
)
print(
    df.dropna(thresh=4)            # thresh=4 this remove all rows except in which row atleast 4 non null value exist EX. we have 6 cols if row contain null values in more then 2 cols that row will remove 
)
print("\n")











# ========================== FILLING NULL VALUES =============================================

print("FILLING NULL VALUES ------------------------------------------------")

print(
    df.fillna(0)                                           # Replacing null values with 0
)
value = {
    "name" : "RRRRR",
    "age" : 50,
    "city" : "Jalandhar",
    "department" : "AI/ML",
    "salary" : 3560300
}
print(
    df.fillna(value=value)                                 # Replacing all null values fillna work with column EX. in column "name" all null value replace with "RRRRR"
)
print(
    df['salary'].fillna(df["salary"].mean().round(2))      # Filling salary with mean of salary && round function round decimal number with 2 EX. 54.6435 => 54.60
)
