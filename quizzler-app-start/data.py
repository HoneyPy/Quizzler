import requests

parameters = {
    "amount":10,
    "type":"boolean"
}

response = requests.get("https://opentdb.com/api.php?amount=10&category=17&type=boolean")
response.raise_for_status()
data = response.json()
question_data = response.json()["results"]


