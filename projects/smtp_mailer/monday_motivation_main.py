import os
import smtplib
import datetime as dt
import random
from dotenv import load_dotenv

load_dotenv()

my_email = "apotiks80@gmail.com"
gmail_password = os.getenv("gmail_password")
res_email = "aalansteel@yahoo.com"

day_of_week = dt.datetime.weekday(dt.datetime.now())


if day_of_week == 0:
    with open("quotes.txt", mode='r') as file:
        quotes_list = file.readlines()

    day_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection_gmail:
        connection_gmail.starttls()
        connection_gmail.login(user=my_email, password=gmail_password)
        connection_gmail.sendmail(
            from_addr=my_email,
            to_addrs=res_email,
            msg=f"Subject:Hello\n\n{day_quote}"
        )
