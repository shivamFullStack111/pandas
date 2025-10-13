import pandas as pd

# -------------------------------
# Create a sample DataFrame
# -------------------------------
data = {
    'Department': ['IT', 'IT', 'HR', 'HR', 'Finance', 'Finance', 'Finance'],
    'Employee': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Salary': [50000, 60000, 45000, 40000, 70000, 72000, 71000],
    'Experience': [2, 3, 5, 2, 4, 6, 5]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# -------------------------------
# Grouping the data by 'Department'
# -------------------------------
grouped = df.groupby('Department')
print("\nGrouped Object:\n", grouped)

# -------------------------------
# Apply Aggregate Functions
# -------------------------------

# 🔹 1. Mean - average salary & experience for each department
print("\nMean (Average) per Department:\n", grouped.mean(numeric_only=True))

# 🔹 2. Sum - total salary & experience for each department
print("\nSum per Department:\n", grouped.sum(numeric_only=True))

# 🔹 3. Count - number of employees in each department
print("\nCount per Department:\n", grouped.count())

# 🔹 4. Min - minimum salary per department
print("\nMinimum Salary per Department:\n", grouped['Salary'].min())

# 🔹 5. Max - maximum salary per department
print("\nMaximum Salary per Department:\n", grouped['Salary'].max())

# 🔹 6. Multiple Aggregations together
print("\nMultiple Aggregations (Salary column):\n", grouped['Salary'].agg(['min', 'max', 'mean', 'sum', 'count']))
