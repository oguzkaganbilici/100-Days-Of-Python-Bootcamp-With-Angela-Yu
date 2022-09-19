import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")

#print(df.head()) # we can see the first 5 rows.

#print(df.shape) # we can see how many columns and rows are there ?

#print(df.columns) # we can see the column's names

#df.isna() # we can detect missing values

#print(df.tail()) # we can see the last 5 columns

clean_df = df.dropna() # to delete missing values

#print(clean_df["Starting Median Salary"]) # to see a particular column

#print(clean_df["Starting Median Salary"].idxmax()) (->43) # to see which id or index has max value

#print(clean_df["Undergraduate Major"].loc[43]) # to see a particular cell
#print(clean_df["Undergraduate Major"][43]) # to see a particular cell

#print(clean_df.loc[43]) # to see all row of 43

#highest_mid_career_dep=clean_df["Undergraduate Major"].loc[clean_df["Mid-Career 10th Percentile Salary"].idxmax()]
#highest_mid_career=clean_df["Mid-Career 10th Percentile Salary"].max()

#lowest_starting_salary_department = clean_df["Undergraduate Major"].loc[clean_df["Starting Median Salary"].idxmin()]
#lowest_starting_salary = clean_df["Starting Median Salary"].min()

#lowest_mid_career_salary_department = clean_df["Undergraduate Major"].loc[clean_df["Mid-Career 10th Percentile Salary"].idxmin()]
#lowest_mid_career_salary = clean_df["Mid-Career 10th Percentile Salary"].min()


#clean_df["Mid-Career 90th Percentile Salary"].subtract(clean_df["Mid-Career 10th Percentile Salary"]) # to take diffence between the two lines

#spread_col = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]
#clean_df.insert(1,"Spread", spread_col) # to add new column

#low_risk = clean_df.sort_values("Spread", ascending=True) # to sort values according to data inside of parenthesis, ascending= True or False 
#print(low_risk[["Undergraduate Major", "Spread"]].head())

#highest_potential = clean_df.sort_values(by="Mid-Career 90th Percentile Salary", ascending=False)
#answer_1 = highest_potential[["Undergraduate Major", "Mid-Career 90th Percentile Salary","Spread"]].head()

#group_counts=clean_df.groupby("Group").count() # to categorieses to datas according to groups

#averages = clean_df.groupby("Group").mean()

#pd.options.display.float_format = "{:,.2f}".format # to display values better

"""
SUMMARY
Use .head(), .tail(), .shape and .columns to explore your DataFrame and find out the number of rows and columns as well as the column names.

Look for NaN (not a number) values with .findna() and consider using .dropna() to clean up your DataFrame.

You can access entire columns of a DataFrame using the square bracket notation: df['column name'] or df[['column name 1', 'column name 2', 'column name 3']]

You can access individual cells in a DataFrame by chaining square brackets df['column name'][index] or using df['column name'].loc[index]

The largest and smallest values, as well as their positions, can be found with methods like .max(), .min(), .idxmax() and .idxmin()

You can sort the DataFrame with .sort_values() and add new columns with .insert()

To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the .groupby() method
"""

