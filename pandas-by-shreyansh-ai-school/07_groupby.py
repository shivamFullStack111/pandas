# groupby() returns a object which we cannot see by print but we can see using for loop

import pandas as pd

data = {
    "department": ["IT", "IT", "Finance", "Finance", "IT", "Finance", "IT", "HR"],
    "employee": ["Aarav", "Vihaan", "Kabir", "Rudra", "Meera", "Isha", "Raj", "Kiran"],
    "salary": [60000, 65000, 50000, 52000, 75000, 72000, 70000, 51000],
    "experience": [2, 4, 3, 5, 6, 4, 3, 2],
    "gender": ["Male", "Male", "Female", "Male", "Female", "Female", "Male", "Female"]

}

df = pd.DataFrame(data)
 
 
 
 
 
 
# =============================== HOW TO SEE DATA OF GROUPBY FUNCTION ============================================================================
print(" PRINTING DATA OF GROUPBY FUNCTION USING FOOR LOOP ------------------------------------------------------------------------------------")

grpData = df.groupby(by="department")           

for index,value in grpData:
    print("index is: ",index)
    print("value is: ",value)
    print("\n")
    
    
    
    

# ====================================== ACCESSING VALUES AND PERFORMING OPERATIONS ==============================================================================================
print(" ACCESSING VALUES AND PERFORMING OPERATIONS ------------------------------------------------------------------------------")

print(
    df.groupby(by="department") ,                                            # Returns a object which we can see by printing using for loop
    "\n"
)        
print(
    df.groupby(by="department")["salary"] ,                                  # This also returns object 
    "\n"
)
print(
    df.groupby(by="department")["salary"].mean(),                            # Finding average salary of each department
    "\n"
)
print(
    df.groupby(by=["department","gender"])["salary"].mean(),                 # Grouping by multiple category in this first categorized by department then furter categorized by gender            
    "\n" 
)

print("\n")




# ====================================== AGGREGATION ==============================================================================================
print(" AGGREGATION ------------------------------------------------------------------------------")



print("\nMean (Average) per Department:\n\n",         df.groupby(by="department")["salary"].mean())                                             # 1. Mean - average salary & experience for each department
print("\nSum per Department:\n\n",                    df.groupby(by="department")["salary"].sum())                                                        # 2. Sum - total salary & experience for each department
print("\nCount per Department:\n\n",                  df.groupby(by="department")["salary"].count())                                            # 3. Count - number of employees in each department
print("\nMinimum Salary per Department:\n\n",         df.groupby(by="department")["salary"].min())                                              # 4. Min - minimum salary per department
print("\nMaximum Salary per Department:\n\n",         df.groupby(by="department")["salary"].max())                                              # 5. Max - maximum salary per department
print("\nMultiple Aggregations (Salary column):\n\n", df.groupby(by="department")["salary"].agg(['min', 'max', 'mean', 'sum', 'count']))        # 6. Multiple Aggregations together







