# 1. Find top 5 columns most correlated with life_expectancy.
# 2. Find average GDP per region and display top 3 richest regions and lowest one.
# 3. Find 5 countries with highest gap between self_employed_pct and vulnerable_employment_pct.
# 4. Drop columns with more than 20% missing values and show new dataset shape.
# 5. Calculate energy_dependence_score = renewable_energy_consumption_pct - fossil_energy_consumption_pct and show top 10 most renewable and most fossil dependent countries.
# 6. Group by democracy_type and find average GDP, life_expectancy, and press score.
# 7. Create population_group (Small, Medium, Large) based on population and find average GDP and internet_pct per group.
# 8. Find correlation between health_expenditure_pct_gdp and life_expectancy and visualize using sns.regplot.
# 9. Find top 10 countries with highest GDP per land_area and calculate their total GDP percentage of world GDP.
# 10. Set 'country' as index and display gdp, life_expectancy, population, internet_pct for India, China, United States, and Japan.



import pandas as pd 

df = pd.read_csv("/home/shivam111/Desktop/pandas/pandas-by-shreyansh-ai-school/countries.csv")

print(df.info())

print("\n")



# ======================== 1. Find top 5 columns most correlated with life_expectancy ===================================

# Correlation between  health_expenditure_pct_gdp life_expectancy 
# Correlation means how two things change together.

# 👉 Agar ek badhe to dusra bhi badhe → positive correlation
# 👉 Agar ek badhe to dusra ghat jaye → negative correlation
top5 = df.corr(numeric_only=True)["life_expectancy"].sort_values(ascending=False).head(5)
print(top5)


print("\n")









# ============== 2. Find average GDP per region and display top 3 richest regions and lowest one. ===========================

gdpAveragePerRegion =  df.groupby(by="region")["gdp"].mean().sort_values(ascending=True)

print(
    "Top 3 richest regions:\n ",
    gdpAveragePerRegion.tail(3),
    "\n"
)

print(
    "Top 3 poorest regions:\n ",
    gdpAveragePerRegion.head(3),
    "\n"
)







# ================  3. Find 5 countries with highest gap between self_employed_pct and vulnerable_employment_pct. ===============

print("Top 5 countries with highest gap between self_employed_pct and vulnerable_employment_pct:\n ",)

print((df["self_employed_pct"]-df["vulnerable_employment_pct"]).sort_values(ascending=False).head(5),)

print("\n")







# ====================  4. Drop columns with more than 20% missing values and show new dataset shape. ==============
print("null-=--------------- \n ",df.isna().sum())
totalRows = df.shape[0]
print(df.shape)
columnsToDrop = df.columns[(df.isna().sum() / totalRows) > 0.2 ]
print("Columns To Drop: \n",columnsToDrop)
df.drop(columns=columnsToDrop,inplace=True)
print(df.shape)