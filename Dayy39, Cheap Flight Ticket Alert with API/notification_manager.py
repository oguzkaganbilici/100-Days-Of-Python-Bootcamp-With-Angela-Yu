import smtplib
from data_manager import DataManager
from flight_data import FlightData

MY_EMAIL = "delykurt@gmail.com"
MY_PASSWORD = "soscqgolxpzqprsb"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    data = DataManager()


    def send_email(self):

        message = f"Subject:Low Price Alert!!\n"
        with smtplib.SMTP("smtp.gmail.com", port = 587) as con:
            con.starttls()
            con.login(MY_EMAIL, MY_PASSWORD)
