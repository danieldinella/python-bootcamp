##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import random
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

TEMPLATES = ["birthday_whisher/letter_templates/letter_1.txt", "birthday_whisher/letter_templates/letter_2.txt", "birthday_whisher/letter_templates/letter_3.txt"]
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")

day = dt.date.today().day
month = dt.date.today().month
df = pd.read_csv("birthday_whisher/birthdays.csv")
people = df.to_dict(orient='records')
bpeople = [person for person in people if person['day'] == day and person['month'] == month]
if len(bpeople) != 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        for bperson in bpeople:
            file = random.choice(TEMPLATES)
            with open(file,'r') as f:
                message = f.read().replace("[NAME]",bperson['name'])
            connection.sendmail(
                from_addr=my_email,
                to_addrs=bperson['email'],
                msg=f"Subject:Happy Birthday!\n\n{message}"
            )
        




