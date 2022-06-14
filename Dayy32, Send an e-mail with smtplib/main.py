##################### Extra Hard Starting Project ######################
import random
import smtplib

import pandas as pd
import datetime as dd
dt = pd.read_csv("birthdays.csv")
today = dd.datetime.today()
today_date = (today.month, today.day)

dt_dict = { (data_row["month"], data_row["day"]) : data_row for (index, data_row) in dt.iterrows()}
print()
if today_date in dt_dict:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as f:
        letter = f.read()
        letter = letter.replace("[NAME]", dt_dict[today_date]["name"])

        my_email = "pythonbotdeneme@gmail.com"
        my_password = "ttchymqwfoyiltuw"
        with smtplib.SMTP("smtp.gmail.com", port=587) as con:
            con.starttls()
            con.login(user=my_email, password=my_password)
            con.sendmail(from_addr=my_email, to_addrs=dt_dict[today_date]["email"], msg=f"Subject:Happy Birthday {dt_dict[today_date]['name']}\n{letter}")
