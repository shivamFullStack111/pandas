import pandas as pd

data = {
    'name':["shivam","karan","manmeet","ankit","navi","mishty","muskan","nandani"],
    'class':"BCA",
    'gender':['male','male','male','male','male','female','female','female']
}

df = pd.DataFrame(data)

print(df['gender'].value_counts())      # This line of code print frequency of all values like males are 5 females are 3
                                        # We can also print frequency by using ["male"] because value_counts return object