import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app_id = os.getenv("APP_ID")
api_nutrionix = os.getenv("API_NUTRITIONIX")
nutritionix_endpoint = os.getenv("NUTRITIONIX_ENDPOINT")
sheety_auth = os.getenv("SHEETY_AUTH")
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

nutritionix_header = {
    "x-app-id" : app_id,
    "x-app-key" : api_nutrionix
}

query = input("Which exercises have you done today? ")

nutritionix_params = {
    "query" : query
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_header)
response.raise_for_status()
data = response.json()["exercises"][0]

day = datetime.now().strftime("%d/%m/%Y")
instant = datetime.now().strftime("%H:%M:%S")
exercise = data["name"].capitalize()
duration = data["duration_min"]
calories = data["nf_calories"]

sheety_params = {
    "workout" : {
        "date" : day,
        "time" : instant,
        "exercise" : exercise,
        "duration" : duration,
        "calories" : calories
    }
}

sheety_header = {
    "Authorization" : sheety_auth
}

response = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_header)
response.raise_for_status()
print(response.text)