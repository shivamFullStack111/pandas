import pandas as pd

fileData = pd.read_csv('files/winequality-red.csv')

print(fileData['chlorides']) # Accessing single column

print(fileData[["pH","alcohol"]]) # Accessing multiple column


