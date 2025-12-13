import smtplib
import datetime as dt
import random
from env_vars import *

day_of_week = dt.datetime.weekday(dt.datetime.now())

email_list = [ceezhar_email, ikenna_email, my_email]

try:
    if day_of_week == 5:
        with open("quotes.txt", mode='r') as file:
            quotes_list = file.readlines()

        day_quote = random.choice(quotes_list)
        for mail in email_list:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection_gmail:
                connection_gmail.starttls()
                connection_gmail.login(user=my_email, password=gmail_password)
                connection_gmail.sendmail(
                    from_addr=my_email,
                    to_addrs=mail,
                    msg=f"Subject: Hello\n\nA lirru motivation for the day\n{day_quote}\nCheers."
                )
        print("success")
except ConnectionError:
    print("Connection Error! Check your internet connection")
except Exception as e:
    print(f"Code Error: {e}")
except smtplib.SMTPException as e:
    print(f"SMTPLIB Error: {e}")