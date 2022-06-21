STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_API ="L9Q5Z1YBEWFN16RP"
NEWS_API = "e800b82e702640ea96d26cfd2ef66bb5"
MY_EMAIL = "delykurt@gmail.com"
MY_PASSWORD = "soscqgolxpzqprsb"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

import requests,smtplib

respond = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={MY_API}")

respond.raise_for_status()
data_json = respond.json()

data = data_json["Time Series (Daily)"]
values = data.items()

yesterday = float(data[list(values)[1][0]]["4. close"])
before_yesterday = float(data[list(values)[2][0]]["4. close"])

if (yesterday - before_yesterday) >= (before_yesterday * 0.05) or (yesterday - before_yesterday) <= -(before_yesterday * 0.05):
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_respond = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2022-06-21&sortBy=popularity&apiKey={NEWS_API}")
    news_respond.raise_for_status()

    news_json = news_respond.json()

    messages = ""
    for i in range(1, 4):
        headline = news_json["articles"][i]["title"]
        brief = news_json["articles"][i]["description"]
        message = f"{headline}\n{brief}\n\n"
        messages += message


    with smtplib.SMTP("smtp.gmail.com", port=587) as con:
        if yesterday >= before_yesterday:
            subject = f"{STOCK}, {round((yesterday - before_yesterday) * 100 / before_yesterday, 2)}% UP"
        else:
            subject = f"{STOCK}, {round((before_yesterday - yesterday) * 100 / before_yesterday, 2  )}% DOWN"
        con.starttls()
        con.login(MY_EMAIL, MY_PASSWORD)
        con.sendmail(from_addr=MY_EMAIL, to_addrs="oguzkaganbilici1@gmail.com", msg=f"Subject:{subject}\n{messages}")



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

