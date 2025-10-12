import pandas as pd

df = pd.read_csv('files/winequality-red.csv')

# Single condition
filterData = df[df['fixed acidity']>7]   # this list all rows which "fixed acidity" greater then 7
print(filterData)

print('\n')

# Multiple conditions 
filterData2 = df[(df['fixed acidity']>7) & (df['fixed acidity']<8) ]   # this list all rows which "fixed acidity" greater then 7 and less then 8
print(filterData2)
