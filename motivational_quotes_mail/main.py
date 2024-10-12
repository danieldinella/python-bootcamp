import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")

today = dt.datetime.now().weekday()
if today == 1:
    with open ("motivational_quotes_mail/quotes.txt","r") as f:
        quotes = [quote.strip() for quote in f]

    todayquote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="daniel.dinella@hotmail.com",
            msg=f"Subject:Hello\n\n{todayquote}"
        )