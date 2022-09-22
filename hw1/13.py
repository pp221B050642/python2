#the next day
import datetime

year = int(input())
month = int(input())
day = int(input())

date = datetime.datetime(year, month, day)

the_next_day = date + datetime.timedelta(1)

print(f"The next date is {the_next_day.strftime('%d-%m-%Y')}")

