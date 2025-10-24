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
import seaborn as sns 
import matplotlib.pyplot as plt 

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







# ====================  4. Drop columns with more than 20% missing values and show new dataset shape. =======================================
totalRows = df.shape[0]

columnsToDrop = df.columns[(df.isna().sum() / totalRows) > 0.2 ]

df.drop(columns=columnsToDrop,inplace=True)

print(df.shape)

print("\n")

# ===========  5. Calculate energy_dependence_score = renewable_energy_consumption_pct - fossil_energy_consumption_pct and show top 10 most renewable and most fossil dependent countries. =======================


df["energy_dependence_score"] = df['renewable_energy_consumption_pct']-df["fossil_energy_consumption_pct"]
 
print("top 10 most renewable and most fossil dependent countries: \n")

print(
    df.nlargest(10,"energy_dependence_score")[["country","energy_dependence_score"]]
)

print("\n")



# ============ 6. Group by democracy_type and find average GDP, life_expectancy, and press score. ===============================================

avg_gdp_by_democracy_type = df.groupby(by="democracy_type")["gdp"].mean()

avg_life_exprectancy_by_democracy_type = df.groupby(by="democracy_type")["life_expectancy"].mean()

avg_press_score_by_democracy_type = df.groupby(by="democracy_type")["press"].mean()


print("Average GDP by democracy type: \n")
print(avg_gdp_by_democracy_type)
print("\n")

print("Average life expectancy by democracy type: \n")
print(avg_life_exprectancy_by_democracy_type)
print("\n")

print("Average press score by democracy type: \n")
print(avg_press_score_by_democracy_type)
print("\n")



# ============== 7. Create population_group (Small, Medium, Large) based on population and find average GDP and internet_pct per group. =============

df["population_group"] = pd.qcut(df["population"],3,labels=["Small","Medium","Large"])

groupedPopulationCategory = df.groupby(by="population_group",observed=False)

avgGDP = groupedPopulationCategory["gdp"].mean()

avgInternetPer = groupedPopulationCategory["internet_pct"].mean()


print("Average GDP based on population group: \n")
print(avgGDP)
print("\n")

print("Average internet percentage based on population group: \n")
print(avgInternetPer)
print("\n")




# ======== 8. Find correlation between health_expenditure_pct_gdp and life_expectancy and visualize using sns.regplot.========================

print("Correlation between health_expenditure_pct_gdp and life_expectancy: \n")

print(
    df["health_expenditure_pct_gdp"].corr(df["life_expectancy"])
)

sns.regplot(data=df, x="health_expenditure_pct_gdp", y="life_expectancy")
plt.title("Health Expenditure vs Life Expectancy")
plt.xlabel("Health Expenditure (% of GDP)")
plt.ylabel("Life Expectancy (years)")
# plt.show()

print("\n")





# ================= 9. Find top 10 countries with highest GDP per land_area and calculate their total GDP percentage of world GDP. ============================

df["gdp_per_land"] = df["gdp"] / df["land_area"] 

top_10_countries_highest_gdp_per_land_area  = df.nlargest(10,"gdp_per_land")[ ["country","gdp_per_land","gdp"] ]

print("Top 10 countries with highest GDP per land_area: ")
print(top_10_countries_highest_gdp_per_land_area)

print("\n")

print("Top 10 countries GDP percentage of world GDP: ")
print(f"{(top_10_countries_highest_gdp_per_land_area["gdp"].sum() / df["gdp"].sum() * 100).round(2)}%")

print("\n")


# ================ 10. Set 'country' as index and display gdp, life_expectancy, population, internet_pct for India, China, United States, and Japan. ===================================

df.set_index("country",inplace=True)

countries = ["India","China","United States","Japan"]    # Indexes
columns = ["gdp", "life_expectancy", "population", "internet_pct"]

data = df.loc[countries,columns]

print("'country' as index and display gdp, life_expectancy, population, internet_pct for India, China, United States, and Japan.: ")
print(data)