import requests
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from data_manager import DataManager

API = "WqQNVH1Yzgw1Km3WyU8beNPb90tb81cx"
DATE_FROM = datetime.now().strftime("%d/%m/%Y")
DATE_TO = (date.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.cities = []
        self.get_cities()

    def get_cities(self):
        data = DataManager()
        self.cities.append(data.cities)
        print(self.cities)



"""       self.url = "https://tequila-api.kiwi.com/v2/search?"
        self.header = {
            "apikey": API
        }
        self.config = {
            "fly_from": "LON",
            "fly_to": self.cities[0],
            "date_from": DATE_FROM,
            "date_to": DATE_TO,
        }
        self.respond = requests.get(url=self.url, params=self.config, headers=self.header)
        print(self.respond.text)
"""