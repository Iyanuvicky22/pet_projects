import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

CURRENT_DATE_FMT = datetime.now().strftime("%Y%m%d")
print(type(CURRENT_DATE_FMT), CURRENT_DATE_FMT)

## ENV VARIABLES
PIXELA_ENDPOINT = os.getenv(key="PIXELA_ENDPOINT")
TOKEN = os.getenv(key="TOKEN")
USER_NAME = os.getenv(key="USER_NAME")
FIRST_GRAPH_ID = os.getenv(key="FIRST_GRAPH_ID")

## ENDPOINTS
graph_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
post_value_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{FIRST_GRAPH_ID}"
update_graph_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{FIRST_GRAPH_ID}/20251211"

## PARAMS
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

graph_params = {
    "id": FIRST_GRAPH_ID,
    "name": "Github Commits Graph",
    "unit": "commit",
    "type": "int",
    "color": "momiji"
}

post_value_params = {
    "date": CURRENT_DATE_FMT,
    "quantity": "2",
}

update_pixel_params = {
    "quantity": "5"
}
## HEADER
header = {
    "X-USER-TOKEN": TOKEN
}


# ## Create User (run once)
# resp = requests.post(url=PIXELA_ENDPOINT,
#                      json=user_params)
# print(resp.text)


# ## Graph Creation
# graph_resp = requests.post(url=graph_endpoint,
#                            json=graph_params,
#                            headers=header)
# print(graph_resp.text)

# ## Post Value to the Graph
# post_resp = requests.post(url=post_value_endpoint,
#                           json=post_value_params,
#                           headers=header)
# print(post_resp.text)

## Update a graph
update_graph_pixel = requests.put(url=update_graph_endpoint,
                          json=update_pixel_params,
                          headers=header)
print(update_graph_pixel.text)
