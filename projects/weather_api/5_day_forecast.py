import requests

URL = "https://api.openweathermap.org/data/2.5/forecast?"
PARAMS = {
    "lat": 7.0,
    "lon": 4.33333,
    "appid": "813729884e6a2563a55305dc7ed7b63f",
    "cnt": 4
}

resp = requests.get(url= URL, params=PARAMS)
resp.raise_for_status()

data = resp.json()
data = data['list']

weather_id_list = []
for time_stamp in data:
    weather_id = time_stamp['weather'][0]['id']
    weather_id_list.append(weather_id)


will_rain = False
if weather_id < 700:
    will_rain = True
    print("There is a chance it will rain today!"
          "\nTake your umbrella bro")
else:
    print("Everywhere clear. Weather cool")