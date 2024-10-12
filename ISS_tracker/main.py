import time
import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_lat = os.getenv("MY_LAT")
my_long = os.getenv("MY_LONG")
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if (my_lat in range(iss_latitude-5,iss_latitude+6) and 
    my_long in range(iss_longitude-5,iss_longitude+6) and 
    (time_now <= sunrise or time_now >= sunset)):
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="daniel.dinella@hotmail.com",
                msg=f"Subject:ISS Above you\n\nLook up!"
            )



