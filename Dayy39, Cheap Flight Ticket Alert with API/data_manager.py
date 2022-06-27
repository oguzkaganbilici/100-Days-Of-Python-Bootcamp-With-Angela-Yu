import requests
from pprint import pprint


API = "https://api.sheety.co/9fad9e21a5ff41c21a3697f64a127874/flightDeals/prices"
PUT_API = "https://api.sheety.co/9fad9e21a5ff41c21a3697f64a127874/flightDeals/prices/"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.cities = []


    def get_cities(self):
        self.respond = requests.get(url=API)
        self.data_json = self.respond.json()
        for i in self.data_json["prices"]:
            self.cities.append(i["city"])

    def change_codes(self):
        for xx in self.cities:
            put_config = {
                "price":
                    {
                        "iataCode": "TESTING"
                    }
            }
            self.put_respond = requests.put(
                url=f"https://api.sheety.co/9fad9e21a5ff41c21a3697f64a127874/flightDeals/prices/{self.cities.index(xx)+ 2}",
                json=put_config)
            print(self.put_respond.text)




