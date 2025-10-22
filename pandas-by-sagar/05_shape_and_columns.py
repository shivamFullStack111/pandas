# shape is attribute which returns number of rows and columns 
# columns is also a attribute which return all columns name 

import pandas as pd

fileData = pd.read_csv('files/winequality-red.csv')
print(fileData.shape)
print(fileData.columns)