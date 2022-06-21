STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_API ="L9Q5Z1YBEWFN16RP"
NEWS_API = "e800b82e702640ea96d26cfd2ef66bb5"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
import requests

respond = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={MY_API}")
respond.raise_for_status()

data_json = respond.json()


data = data_json["Time Series (Daily)"]
values = data.items()

yesterday = float(data[list(values)[1][0]]["4. close"])
before_yesterday = float(data[list(values)[2][0]]["4. close"])

print(yesterday, before_yesterday)
if (yesterday - before_yesterday) >= (before_yesterday * 5/100) or (yesterday - before_yesterday) <= -(before_yesterday * 5/100):
    print("news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_respond = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2022-06-21&sortBy=popularity&apiKey={NEWS_API}")
news_respond.raise_for_status()

news_json = news_respond.json()

print(news_json["articles"][0]["description"])
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

