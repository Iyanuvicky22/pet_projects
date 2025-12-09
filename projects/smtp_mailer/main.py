##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

# connection
my_email = "apotiks80@gmail.com"
gmail_password = "uvhojvsdqgsnfabp"

# 1. Update the birthdays.csv
file_path = r"birthdays.csv"
data = pd.read_csv(file_path)

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_tuple = (today.month, today.day)
new_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

try:
    if today_tuple in new_dict.keys():
        birthday_person = new_dict[today_tuple]
        birthday_person_name = birthday_person['name']
        birthday_person_email = birthday_person['email']
        letter_filepath = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(letter_filepath) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person_name)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=gmail_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_person_email,
                msg=f"Subject: Happy Birthday {birthday_person_name}\n\n{contents}"
            )
except FileNotFoundError:
    file_path = r"birthdays.csv"
    data = pd.read_csv(file_path)





