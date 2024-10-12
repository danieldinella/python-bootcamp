import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

latitude = os.getenv("LATITUDE")
longitude = os.getenv("LONGITUDE")
api_key = os.getenv("API_KEY")
twilio_sid = os.getenv("TWILIO_SID")
twilio_auth = os.getenv("TWILIO_AUTH")

CNT = 4
parameters = {
    "lat" : latitude,
    "lon" : longitude,
    "appid" : api_key,
    "cnt" : CNT
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
codes = [data['list'][i]['weather'][0]['id'] for i in range(4)]
for code in codes:
    if code < 700:
        client = Client(twilio_sid,twilio_auth)
        message = client.messages \
            .create(
                body="It's going to rain! Bring an umbrella.",
                from_="+18503317359",
                to="+393478174209"
        )
        break