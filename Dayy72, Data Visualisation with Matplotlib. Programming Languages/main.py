import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("QueryResults.csv", names=["DATE","TAG","POSTS"],header=0)
# df.rename(columns={"m":"DATE","TagName":"TAG","Unnamed: 2":"POSTS"}, inplace=True)
# üstteki kodun yerine read_csv icinde names=["asdad","asdads"] ile tanımlayabiliriz


#count_of_row = len(df) # to learn number of rows
#count_of_col = len(df.columns)
counts = df.shape # üsttekileri kısaca verir.
count_of_all = df.count()

counts_of_posts = df.groupby("TAG").sum().sort_values(by="POSTS", ascending=False)
dates_of_posts = df.groupby("TAG").count()

df["DATE"] = pd.to_datetime(df["DATE"]) # to convert our date column

reshaped_df = df.pivot(index="DATE",columns="TAG",values="POSTS")
print(f"size of reshaped_df=rows:{reshaped_df.shape[0]},columns:{reshaped_df.shape[1]}")
print("columns:", reshaped_df.columns)
reshaped_df.fillna(0, inplace=True)
print("Count the number of entries per column:", reshaped_df.count())



plt.figure(figsize=(16,10)) #16 width 10 height
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.ylim(0, 35000)
# .figure() # allows us to resize our chart
# .xticks() # configures our x-axis
# .yticks() # configures our y-axis
# .xlabel() # add text to the x-axis
# .ylabel() # add text to the y-axis
# .ylim()   # allows us to set a lower and upper bound  
for i in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[i], linewidth=3, 
             label=reshaped_df[i].name)

plt.legend(fontsize=16) #plt.show() yerine kullandık coklu chartlarda.
#%%
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("QueryResults.csv", names=["DATE","TAG","POSTS"],header=0)
# df.rename(columns={"m":"DATE","TagName":"TAG","Unnamed: 2":"POSTS"}, inplace=True)
# üstteki kodun yerine read_csv icinde names=["asdad","asdads"] ile tanımlayabiliriz


#count_of_row = len(df) # to learn number of rows
#count_of_col = len(df.columns)
counts = df.shape # üsttekileri kısaca verir.
count_of_all = df.count()

counts_of_posts = df.groupby("TAG").sum().sort_values(by="POSTS", ascending=False)
dates_of_posts = df.groupby("TAG").count()

df["DATE"] = pd.to_datetime(df["DATE"]) # to convert our date column

reshaped_df = df.pivot(index="DATE",columns="TAG",values="POSTS")
print(f"size of reshaped_df=rows:{reshaped_df.shape[0]},columns:{reshaped_df.shape[1]}")
print("columns:", reshaped_df.columns)
reshaped_df.fillna(0, inplace=True)
print("Count the number of entries per column:", reshaped_df.count())


roll_df = reshaped_df.rolling(window=6).mean() # to make lines smoother

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.ylim(0, 35000)

for col in roll_df.columns:
    plt.plot(roll_df.index, roll_df[col], linewidth=3, label=roll_df[col].name)
    
    
plt.legend(fontsize=16)



"""
                            SUMMARISE
used .groupby() to explore the number of posts and entries per programming language

converted strings to Datetime objects with to_datetime() for easier plotting

reshaped our DataFrame by converting categories to columns using .pivot()

used .count() and isna().values.any() to look for NaN values in our DataFrame, which we then replaced using .fillna()

created (multiple) line charts using .plot() with a for-loop

styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.

added a legend to tell apart which line is which by colour

smoothed out our time-series observations with .rolling().mean() and plotted them to better identify trends over time.
"""




 


