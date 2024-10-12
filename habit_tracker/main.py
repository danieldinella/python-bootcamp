import requests
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()

GRAPHID = "graph1"
token = os.getenv("TOKEN")
username = os.getenv("USERNAME")
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : token,
    "username" : username,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}


graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id" : GRAPHID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-token" : token,
}

pixel_endpoint = f"{graph_endpoint}/{GRAPHID}"
pixel_config = {
    "date" : date.today().strftime("%Y%m%d"),
    "quantity" : "2"
}

update_endpoint = f"{pixel_endpoint}/20241010"
update_config = {
    "quantity" : "1"
}

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)