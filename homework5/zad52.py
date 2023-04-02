#!/usr/bin/python3
import datetime

def print_working_days(date1, date2):
    number_of_working_days = 0
    format = '%Y-%m-%d'  # The format
    date1_datetime = datetime.datetime.strptime(date1, format)
    date2_datetime = datetime.datetime.strptime(date2, format)
    while date1_datetime < date2_datetime:
        if date1_datetime.weekday() <= 4: #0 to poniedziałek, 4 to piątek, czyli liczymy dzi od 0 do 4 jako pracujące
            number_of_working_days = number_of_working_days + 1
        date1_datetime = date1_datetime + datetime.timedelta(days = 1)
    print(number_of_working_days)

print_working_days("2023-01-01","2023-12-31")
input()