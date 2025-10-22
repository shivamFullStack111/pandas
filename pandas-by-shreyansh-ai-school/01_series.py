# Series is a datatype in python like array but array is horizontal and series is verticle 
# Series contain 2 thing index/labels and values 
# We can create series by array, typle, dictionary etc

import numpy as np 
import pandas as pd 

# ============================== CREATING SERIES ==========================================

# ---------------- Creating using array --------------------------
arr = [10,20,30]
lbls = ["a","b","c"]

series1 = pd.Series(data=arr,index=lbls)
print(series1)        
print(series1.index,series1.values)    # Accessing key and values individually 


# ---------------- Creating using dictionary ------------------------
dic = {                  
    "a":43,
    "b":65,
    "c":67
}

series2 = pd.Series(dic)     # Index create from key of dictionary
print(series2)