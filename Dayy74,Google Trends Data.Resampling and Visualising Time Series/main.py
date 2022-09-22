import pandas as pd
import matplotlib.pyplot as plt


df_tesla = pd.read_csv("TESLA Search Trend vs Price.csv")
df_unemployment = pd.read_csv("UE Benefits Search vs UE Rate 2004-19.csv")
df_btc_price = pd.read_csv("Daily Bitcoin Price.csv")
df_btc_search = pd.read_csv("Bitcoin Search Trend.csv")

print("for tesla, null values are", df_tesla.isnull().values.any())
print("for unemployment, null values are", df_unemployment.isnull().values.any())
print("for btc price, null values are", df_btc_price.isnull().values.any())
print("for btc search, null values are", df_btc_search.isnull().values.any())

print("for btc price, null values are", df_btc_price.isnull().values.sum())

df_btc_price.dropna(inplace=True)

df_tesla["MONTH"] = pd.to_datetime(df_tesla["MONTH"])
df_unemployment["MONTH"] = pd.to_datetime(df_unemployment["MONTH"])
df_btc_search["MONTH"] = pd.to_datetime(df_btc_search["MONTH"])
df_btc_price["DATE"] = pd.to_datetime(df_btc_price["DATE"])

df_btc_price_monthly = df_btc_price.resample("M", on="DATE").last()

"""
import matplotlib.dates as mdates
does not work for me
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_frmt = mdates.DateFormatter('%Y-%m')

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax1.xaxis.set_minor_locator(months)"""


"""
#plots
plt.figure(figsize=(14,8), dpi=120)
plt.xticks(fontsize=14,rotation=45)
plt.yticks(fontsize=14)
plt.title("Tesla Web Search vs Price", fontsize=18)


ax1 = plt.gca()
ax2 = plt.twinx()

ax1.set_ylim([0,600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
ax2.set_ylim([0,33])



ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE,  color="#FF2611", lw=4)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color="#33D1FF", lw=4)
ax1.set_xlabel("Years")
ax1.set_ylabel("TSLA Stock Price",color="#FF2611")
ax2.set_ylabel("Search Trend",color="#33D1FF")
plt.show()
------------------------------------------------------------
plt.figure(figsize=(16,10), dpi=120)
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)

ax1 = plt.gca()
ax2 = plt.twinx()

plt.title("Bitcoin News Search vs Resampled Price", fontsize=19)
ax1.set_xlabel("Years")
ax1.set_ylabel("BTC Price", color="orange", fontsize=16)
ax2.set_ylabel("Search Trend", color="#6fa8dc", fontsize=16)

ax1.set_ylim(bottom=0, top=15000)
ax1.set_xlim([df_btc_price_monthly.index.min(),df_btc_price_monthly.index.max()])


ax1.plot(df_btc_price_monthly.DATE, df_btc_price_monthly.CLOSE, color="orange",
         lw=4, markersize=10, linestyle="--")
ax2.plot(df_btc_search.MONTH, df_btc_search.BTC_NEWS_SEARCH, color="#6fa8dc",
         lw=2, marker="o", markersize=7)
------------------------------------------------------------------
"""
plt.figure(figsize=(12,8), dpi=120)
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)


roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()

ax1 = plt.gca()
ax2 = plt.twinx()
ax1.grid(color="grey", linestyle="--")

plt.title("Monthly Search of 'Unemployment Benefits' in the U.S. vs the U/E Rate", fontsize=19)
ax1.set_xlabel("Years")
ax1.set_ylabel("Unemployment Benefits Web Search", color="orange", fontsize=16)
ax2.set_ylabel("Unemployment Rates", color="#6fa8dc", fontsize=16)



ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
ax1.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, color="orange",
         lw=2, markersize=8, linestyle="--")
ax2.plot(df_unemployment.MONTH, roll_df.UNRATE, color="#6fa8dc",
         lw=2, marker="o", markersize=5)

#%%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("UE Benefits Search vs UE Rate 2004-20.csv")

df["MONTH"] = pd.to_datetime(df["MONTH"])


plt.figure(figsize=(12,8), dpi=120)

ax1=plt.gca()
ax2=plt.twinx()
ax1.set_ylabel("Unemployment Web Searchs")
ax2.set_ylabel("Unemployment Rates")
ax1.set_xlabel("Years")

ax1.set_xlim([df.MONTH.min(), df.MONTH.max()])

ax1.plot(df.MONTH, df.UE_BENEFITS_WEB_SEARCH, color="b")
ax2.plot(df.MONTH, df.UNRATE, color="r")
plt.show()


"""
                            SUMMARISE
            
How to use .describe() to quickly see some descriptive statistics at a glance.

How to use .resample() to make a time-series data comparable to another by changing the periodicity.

How to work with matplotlib.dates Locators to better style a timeline (e.g., an axis on a chart).

How to find the number of NaN values with .isna().values.sum()

How to change the resolution of a chart using the figure's dpi

How to create dashed '--' and dotted '-.' lines using linestyles

How to use different kinds of markers (e.g., 'o' or '^') on charts.

Fine-tuning the styling of Matplotlib charts by using limits, labels, linewidth and colours (both in the form of named colours and HEX codes).

Using .grid() to help visually identify seasonality in a time series.

"""