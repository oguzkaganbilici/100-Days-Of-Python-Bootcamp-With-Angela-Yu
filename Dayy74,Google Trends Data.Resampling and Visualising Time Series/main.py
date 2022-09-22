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

#plots
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14,rotation=45)
plt.yticks(fontsize=14)
plt.title("Tesla Web Search vs Price")

ax1 = plt.gca()
ax2 = plt.twinx()

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color="#FF2611",lw=4)
ax2.plot(df_tesla.MONTH,df_tesla.TSLA_WEB_SEARCH, color="#33D1FF",lw=4)
ax1.set_xlabel("Years")
ax1.set_ylabel("TSLA Stock Price",color="#FF2611")
ax2.set_ylabel("Search Trend",color="#33D1FF")