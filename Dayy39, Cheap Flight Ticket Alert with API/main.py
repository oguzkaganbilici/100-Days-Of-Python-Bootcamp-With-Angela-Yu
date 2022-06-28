#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_data import FlightData

data1 = DataManager()

f1 = FlightData()
print(f1.find_cheap_flight(data1.codes))



