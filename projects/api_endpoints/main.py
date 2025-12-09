import requests

response = requests.get(url="http://api.open-notify.org//iss-now.json")
response.raise_for_status()

data = response.json()
print(data)

long = data['iss_position']['longitude']
lat = data['iss_position']['latitude']

iss_pos = (long, lat)
print(iss_pos)