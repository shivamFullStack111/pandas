import pandas as pd 

data = pd.read_csv("files/winequality-red.csv")

df = pd.DataFrame(data)

print(df.info())