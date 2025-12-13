import requests

params = {
    "amount": 20,
    "type": "boolean",
    "category": 18
}
resp = requests.get("https://opentdb.com/api.php", params=params)
resp.raise_for_status()

data = resp.json()
question_data = data['results']
