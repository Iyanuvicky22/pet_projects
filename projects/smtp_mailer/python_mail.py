



import datetime as dt

print(dt.datetime.now())
now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()

if 2019 <= year == 2020:
    print("Wear a nose mask!")
else:
    print("You might be in the clear")
    print(year)

date_of_birth = dt.datetime(year=1997, month=2, day=15)
print(f"I was born on {date_of_birth}")