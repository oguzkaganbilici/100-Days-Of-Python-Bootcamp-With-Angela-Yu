import requests

end_point = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
data_json = end_point.json()

question_data = data_json["results"]