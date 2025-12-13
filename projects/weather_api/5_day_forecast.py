import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.openweathermap.org/data/2.5/forecast?"
APP_ID = os.getenv("APP_ID")
PARAMS = {
    "lat": 7.0,
    "lon": 4.33333,
    "appid": APP_ID ,
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