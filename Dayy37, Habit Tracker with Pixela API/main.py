import requests
import datetime

pixela_api = "https://pixe.la/v1/users"


TOKEN = "helloWorld"
USERNAME = "oguzkaganbilici"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#respond = requests.post(url=pixela_api, json=user_params)
"""
graph_endpoint = f"{pixela_api}/{USERNAME}/graphs"

graph_config = {
                "id":"graph1",
                "name":"Python Graph",
                "unit":"Day",
                "type":"int",
                "color":"ajisai"
                }

headers = {
    "X-USER-TOKEN": TOKEN
}
respond = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(respond.text)
"""
#endpoint = f"{pixela_api}/{USERNAME}/graphs/graph1"
headers = {
    "X-USER-TOKEN": TOKEN
}
today = datetime.datetime.now()
xx = today.strftime('%Y%m%d')
"""configs = {
        "date": today.strftime('%Y%m%d'),
        "quantity": "100",
    }"""

put_configs = {
    "quantity": "100000",
}
endpoint = f"{pixela_api}/{USERNAME}/graphs/graph1/{xx}"

respond = requests.put(url=endpoint, json=put_configs, headers=headers)

print(respond.text)

