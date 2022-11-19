"""
import requests

API_TOKEN = "b698d5ccb97c8ac8be1bbdf572531dc91a4d822d"
API_TOKEN = "b698d5ccb97c8ac8be1bbdf572531dc91a4d822d"

URL = "https://owlbot.info/api/v4/dictionary/owl"

def search(word):
    url = f"https://owlbot.info/api/v4/dictionary/{word}"
    headers = {
        "Authorization": f"Token {API_TOKEN}"
    }
    res = requests.get(url=url, headers=headers)

    return res.json()


"""
# Oxford dict API
import requests

API_TOKEN = "69abc94fc862fed424aff13ada58f155"
APP_ID = "b454617e"


def search(word):
    language = "en-gb"
    URL = f"https://od-api.oxforddictionaries.com/api/v2/entries/{language}/{word}"
    params = {
        "app_id": APP_ID,
        "app_key": API_TOKEN
    }
    res = requests.get(url=URL, headers=params)

    return res.json()


