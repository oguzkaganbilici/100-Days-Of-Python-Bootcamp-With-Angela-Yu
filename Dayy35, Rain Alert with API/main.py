import requests
import smtplib

api_key = "0924586a753cf92a4b1106a66ba57570"
my_lat = 40.985859
my_lon = 7.879799
exclude = "current,minutely,daily"

respond = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={my_lat}&lon={my_lon}&exclude={exclude}&appid={api_key}")
respond.raise_for_status()

data_json = respond.json()

data_dict = data_json["hourly"][:12]
will_rain = False

for i in data_dict:
    condition_code = i["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    my_email = "pythonbotdeneme@gmail.com"
    my_password = "ttchymqwfoyiltuw"
    with smtplib.SMTP("smtp.gmail.com", port=587) as con:
        con.starttls()
        con.login(my_email, my_password)
        con.sendmail(from_addr=my_email, to_addrs="oguzkaganbilici1@gmail.com", msg="Subject:Warning!\nTake an umbrella, it is going to rain!")
else:
    my_email = "pythonbotdeneme@gmail.com"
    my_password = "ttchymqwfoyiltuw"
    with smtplib.SMTP("smtp.gmail.com", port=587) as con:
        con.starttls()
        con.login(my_email, my_password)
        con.sendmail(from_addr=my_email, to_addrs="oguzkaganbilici1@gmail.com", msg="Subject:Good Morning!\nIt's going to be amazing day. Have fun!")


