import requests
from datetime import datetime

APP_ID = "8b64bd59"
APP_KEY = "87c244a845bd583c8f2b98439fb025c2"
SHEETY_USERNAME = "oguzkaganbilici"
SHEETY_PASS = "helloWorld"
SHEETY_TOKEN = "Basic b2d1emthZ2FuYmlsaWNpOmhlbGxvV29ybGQ="

while 1:
    exercise = input("What exercise you did: ")

    n_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
    n_headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
    }
    n_params = {
        "query": exercise,
        "gender": "male",
        "weight_kg": 63,
        "height_cm": 178,
        "age": 25
    }
    n_respond = requests.post(url=n_url, json=n_params, headers=n_headers)
    n_data = n_respond.json()

    s_url = "https://api.sheety.co/9fad9e21a5ff41c21a3697f64a127874/myWorkouts/sayfa1"
    today = datetime.today()
    str_today = today.strftime("%d/%m/%Y")
    now = datetime.now()
    str_now = now.strftime("%H:%M:%S")
    s_params = {
        "sayfa1": {
            #all keys must be lower case, its rule
            "date": str_today,
            "time": str_now,
            "exercise": n_data["exercises"][0]["user_input"].title(),
            "duration": n_data["exercises"][0]["duration_min"],
            "calories": n_data["exercises"][0]["nf_calories"],
        }
    }
    s_headers = {
        "Authorization": SHEETY_TOKEN
    }
    s_respond = requests.post(url=s_url, json=s_params, headers=s_headers)
    print(s_respond.text)
