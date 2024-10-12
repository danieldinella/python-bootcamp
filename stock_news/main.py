import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

alpha_api = os.getenv("ALPHA_API")
news_api = os.getenv("NEWS_API")
twilio_sid = os.getenv("TWILIO_SID")
twilio_auth = os.getenv("TWILIO_AUTH")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_PARAMS = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : alpha_api
}



alpha_response = requests.get(url="https://www.alphavantage.co/query", params=ALPHA_PARAMS)
alpha_response.raise_for_status()
days = list(alpha_response.json()['Time Series (Daily)'].items())

first_day_date = days[0][0]
first_day_close = float(days[0][1]['4. close'])
second_day_date = days[1][0]
second_day_close = float(days[1][1]['4. close'])

difference = first_day_close - second_day_close
percentage = difference * second_day_close / 100

if percentage >= 5 or percentage <= -5:
    news_params = {
        "qInTitle" : COMPANY_NAME,
        "apiKey" : news_api
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    article = news_response.json()["articles"][0]
    if percentage >= 0:
        title = f"{STOCK}: +{round(abs(percentage))}"
    else:
        title = f"{STOCK}: -{round(abs(percentage))}"
    headline = f"Headline: {article['title']}"
    brief = f"Brief: {article['description']}"
    client = Client(twilio_sid, twilio_auth)
    message = client.messages \
        .create(
            body=f"{title}\n{headline}\n{brief}",
            from_="+18503317359",
            to="+393478174209"
        )


