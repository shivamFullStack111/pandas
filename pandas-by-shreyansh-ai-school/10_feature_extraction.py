# QUS 1: make a new column for episode count
# QUS 2: make a new column for time stamp
# QUS 3: make a new column for members
# QUS 4: which anime has the highest score
# QUS 5: give me top 5 highest scoring anime
# QUS 6: which anime has the highest episode count
# QUS 7: animes with top 5 episode count
# QUS 8: which is the longest running anime



import pandas as pd 

df = pd.read_csv("/home/shivam111/Desktop/pandas/pandas-by-shreyansh-ai-school/anime.csv")

# ============================= EXTRACTING TOTAL EPISODES ============================================

# In this block i am extracting total episodes from title column 

# Function to extract episodes like "53 eps" from title
def extractEpisode(title):
    
    totalEpisodes = ""
    flag = False
    
    for i in title:
        if flag == True:
            if i == ")":
                return totalEpisodes
            totalEpisodes+=i 
        if i == "(":
            flag = True
          
        
df["episodes"] = df["Title"].apply(extractEpisode)
df["episodes"] = df["episodes"].apply(lambda x: x.split(" ")[0]).astype(int)

print("New episodes column added: \n ",df.head(5))
print("\n")



# ============================= EXTRACTING TIME OF SERIES ============================================

# Function to extract time like "Apr 2011 - Sep 2011" from title
def extractTime(text):
    
    flag = False 
    time = ""
    
    for i in text:
        if flag:
            time+=i
        if i == ")":
            flag = True 
        
    return time[0:19]

df["duration"]=extractTime("Steins;GateTV (24 eps)Apr 2011 - Sep 20112,473,707 members")
print("New duration column added: \n ",df.head(5))

print("\n")





# ============================= EXTRACTING MEMBERS OF SERIES ============================================

# Function to extract members like "182,450 members" from title
def extractMembers(text):
    text = text.split(" members")[0]
    text = text.split(")")[1]
    return int(text[19:].replace(",",""))
    
df["members"] = df["Title"].apply(extractMembers)
print("New members column added: \n ",df.head(5))


print("\n")





# ======================================== DURATION IN MONTHS ================================================================

# Input: duration string like 'Apr 2011 - Mar 2012'
def calculate_total_months(duration):
    
    # Split the string into start and end
    start_str, end_str = duration.split(" - ")

    # Convert to datetime
    start_date = pd.to_datetime(start_str, format="%b %Y")
    end_date = pd.to_datetime(end_str, format="%b %Y")

    # Calculate total months (inclusive)
    total_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month + 1)
    return total_months

df["total_months"] = df["duration"].apply(calculate_total_months)

print("New total_months column added: \n ",df.head(5))


print("\n")


# ========================================== HIGHEST SCORED ANIME ===============================================

print(
    "Highest score anime: \n ",
    df[df["Score"]==df["Score"].max()]
)


# ======================================== TOP 5 HIGHEST SCORED ANIME ===========================================

print("Top 5 higest scored anime: \n")
print(df.nlargest(5, "Score"))                # 1) nlargest() => for DESC Order 2) nsmallest() =>  for ASC Order

print("\n")


# ======================================== ANIME WITH MOST EPISODES ===========================================

print("Anime with most episodes: \n")
print(df.nlargest(1,"episodes")[["Rank","Title","episodes"]])

print("\n")


# ======================================== TOP 5 ANIME WITH MOST EPISODES ===========================================

print("Top 5 anime with most episodes: \n")
print(df.nlargest(5,"episodes")[["Rank","Title","episodes"]])

print("\n")


# ======================================== LONGEST RUNNING ANIME ===========================================

print("Longest running anime: \n")
print(df.nlargest(1,"total_months"))

print("\n")

