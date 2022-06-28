import requests

API = "WqQNVH1Yzgw1Km3WyU8beNPb90tb81cx"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def find_codes(self, city_name):
        url = "https://tequila-api.kiwi.com/locations/query"
        header = {
            "apikey": API
        }
        query = {"term": city_name, "location_types": "city"}
        respond = requests.get(url=url, params=query, headers=header)
        result = respond.json()["locations"][0]["code"]
        return result




