import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 41.033020 # Your latitude
MY_LONG = 37.496159 # Your longitude


def check():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if (MY_LONG + 5 >= iss_longitude >= MY_LONG - 5) and (MY_LAT + 5 >= iss_latitude >= MY_LAT - 5):
        if time_now.hour >= sunset or time_now.hour <= sunrise:
            return 1


def send_mail():
    aa = check()
    if aa:
        my_email = "pythonbotdeneme@gmail.com"
        my_password = "ttchymqwfoyiltuw"
        with smtplib.SMTP("smtp.gmail.com", port=587) as f:
            f.starttls()
            f.login(my_email, my_password)
            f.sendmail(from_addr=my_email, to_addrs="oguzkaganbilici1@gmail.com",
                       msg="Subject:Hey\nLook up the sky! It's above you!")


while 1:
    time_now = datetime.now()
    sec = time_now.second
    send_mail()
    time.sleep(60)





















#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



