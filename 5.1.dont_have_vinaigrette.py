from datetime import date, datetime
import datetime
import random

date1 = input("enter a date of form YYYY-MM-DD: ")
date2 = input("enter a date of form YYYY-MM-DD: ")

if date1 > date2:
    temp = date1
    date1 = date2
    date2 = temp

date_object1 = (datetime.datetime.strptime(date1, "%Y-%m-%d")).date()
date_object2 = (datetime.datetime.strptime(date2, "%Y-%m-%d")).date()
dif = (date_object2-date_object1).days
random_number_of_days = random.randrange(dif)
random_date = date_object1 + datetime.timedelta(days=random_number_of_days)
print(random_date)
if random_date.weekday() == 0:  # if it is monday
    print("אין לי וינגרט")



