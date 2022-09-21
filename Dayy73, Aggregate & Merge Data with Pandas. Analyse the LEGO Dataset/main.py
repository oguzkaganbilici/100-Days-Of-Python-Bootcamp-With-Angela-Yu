import pandas as pd

color_df = pd.read_csv("data/colors.csv")
lego_df = pd.read_csv("data/sets.csv")


count_of_colors = color_df["name"].nunique() # len(color_df["name"].unique().tolist())
count_of_trans = color_df["is_trans"].value_counts()

the_first_lego_year = lego_df["year"].min()
the_first_lego = lego_df["name"].loc[lego_df["year"].idxmin()]

how_many_products_in_first_year = lego_df["name"].loc[lego_df["year"] == the_first_lego_year].nunique()
the_most_number_of_parts = lego_df.sort_values(by=["num_parts"], ascending=False)[0:5]

#%%

import pandas as pd
import matplotlib.pyplot as plt


color_df = pd.read_csv("data/colors.csv")
lego_df = pd.read_csv("data/sets.csv")

sets_by_year = lego_df.groupby("year").count()["set_num"]


plt.figure(figsize=(12,10))
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.plot(sets_by_year.index[0:-2], sets_by_year.values[0:-2])
#%%
import pandas as pd
import matplotlib.pyplot as plt


color_df = pd.read_csv("data/colors.csv")
lego_df = pd.read_csv("data/sets.csv")


sets_by_year = lego_df.groupby("year").count()["set_num"]
themes_by_year = lego_df.groupby("year").agg({"theme_id":pd.Series.nunique})
themes_by_year.rename(columns= {"theme_id":"nr_themes"}, inplace=True)

#sag tarafta da bir eksen yaratmak icin

ax1=plt.gca() #get current axes
ax2=plt.twinx() #create another axis that shares the same x-axis

ax1.plot(sets_by_year.index[:-2], sets_by_year.values[:-2], color="r")
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color="b")
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of sets", color="red")
ax2.set_ylabel("Number of themes", color="blue")





