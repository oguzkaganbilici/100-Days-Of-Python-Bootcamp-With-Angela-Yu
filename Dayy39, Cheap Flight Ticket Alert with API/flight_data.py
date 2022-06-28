import requests
from data_manager import DataManager
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

API = "WqQNVH1Yzgw1Km3WyU8beNPb90tb81cx"
DATE_FROM = datetime.now().strftime("%d/%m/%Y")
DATE_TO = (date.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")

class FlightData:
    #This class is responsible for structuring the flight data.
    def find_cheap_flight(self, codes=list):
        url = "https://tequila-api.kiwi.com/v2/search"

        min_prices = {}
        header = {
            "apikey": API
        }
        for xx in codes:
            prices = {}
            config = {
                "fly_from": "LON",
                "fly_to": xx,
                "date_from ": DATE_FROM,
                "date_to ": DATE_TO
            }

            responds = requests.get(url=url, headers=header, params=config)
            data = responds.json()["data"]
            for i in data:
                print(prices)

