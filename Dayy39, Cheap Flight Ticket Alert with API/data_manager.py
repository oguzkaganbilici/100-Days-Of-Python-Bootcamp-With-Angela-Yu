import requests
from flight_search import FlightSearch


API = "https://api.sheety.co/ee5aa4e3e09d41b039fa00a8468c100d/flightDeals/prices"
PUT_API = "https://api.sheety.co/ee5aa4e3e09d41b039fa00a8468c100d/flightDeals/prices/"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.cities = []
        self.codes = []
        self.get_cities()
        #self.change_codes()
        self.get_codes()

    def get_cities(self):
        self.respond = requests.get(url=API)
        self.data_json = self.respond.json()
        for i in self.data_json["prices"]:
            self.cities.append(i["city"])

    def get_codes(self):
        self.respond = requests.get(url=API)
        self.data_json = self.respond.json()
        for i in self.data_json["prices"]:
            self.codes.append(i["iataCode"])
        return self.codes

    def change_codes(self):
        f1 = FlightSearch()
        for xx in self.cities:
            put_config = {
                "price":
                    {
                        "iataCode": f1.find_codes(xx)
                    }
            }
            self.put_respond = requests.put(
                url=f"https://api.sheety.co/9fad9e21a5ff41c21a3697f64a127874/flightDeals/prices/{self.cities.index(xx)+ 2}",
                json=put_config)
            print(self.put_respond.text)




