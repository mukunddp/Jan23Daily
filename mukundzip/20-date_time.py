import datetime
import time

# print(time.time())
# print(datetime.datetime.fromtimestamp(1675515663.3996978))
# time.sleep(30)
# # datetime.datetime.isocalendar()
# print(time.gmtime())


# print(time.gmtime())
# print(datetime.date.today())
#
# print(datetime.date.today().strftime("%d - %m - %Y"))
# # %d == date in format of number
# # %m == month in format of number
# # %Y == year in number four digits
# # %y == year in number two digits
# # %B == month in word format
#
#
#
#
# # # "%B, %d, %Y"
# print(datetime.date.today().strftime("%d %B, %Y"))
# # # "%m / %d / %y"
# print(datetime.date.today().strftime("%m / %d / %y"))
# # # "%b - %d - %Y"
# # print(datetime.date.today().strftime("%m - %d - %Y"))






# using datetime module
# import datetime
#
# # ct stores current time
# ct = datetime.datetime.today()
# print("current time:-", ct)
#
# # ts store timestamp of current time
# ts = ct.timestamp()
# print("timestamp:-", ts)

# Python program to demonstrate
#  datetime module
#
#
#

# import datetime
#
# dt = datetime.date(2020, 1, 26)
# # prints the date as date
# # object
# print(dt)
#
# # prints the current date
# print(datetime.date.today())
#
# # prints the date and time
# dt = datetime.datetime(1998, 12, 30, 15, 14, 12, 342380)
# print(dt)
# print(dt.timestamp())
# ts = 1615045692.34238
# asasasa = datetime.datetime.fromtimestamp(ts)
# print(asasasa)


#
# # prints the current date
# # and time
# print(datetime.datetime.now())
#
#
#
#
#
# UTC - Universal Time Coordinated
from datetime import timezone
import datetime

# Getting the current date
# and time
# dt = datetime.datetime.now(timezone.utc)
#
# from datetime import datetime
# import pytz
#
# # get the standard UTC time
# UTC = pytz.utc
#
# # it will get the time zone
# # of the specified location
# IST = pytz.timezone('Asia/Kolkata')
#
# # print the date and time in
# # standard format
# print("UTC in Default Format : ",
#       datetime.now(UTC))
#
# print("IST in Default Format : ",
#       datetime.now(IST))
#
# # print the date and time in
# # specified format
# datetime_utc = datetime.now(UTC)
# print("Date & Time in UTC : ",
#       datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
#
# datetime_ist = datetime.now(IST)
# print("Date & Time in IST : ",
#       datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
#
# #
# #
#
#
# # Python3 program to find number of days
# # between two given dates
# from datetime import date
#
#
# def numOfDays(date1, date2):
#     return (date2 - date1).days
#
#
# # Driver program
# date1 = date(2018, 12, 13)
# date2 = date(2019, 2, 25)
# print(numOfDays(date1, date2), "days")
#
#
#
#
#
# # Python3 code to demonstrate working of
# # Random K dates in Range
# # Using choices() + timedelta() + loop
# from datetime import date, timedelta
# from random import choices
#
# # initializing dates ranges
# test_date1, test_date2 = date(2015, 6, 3), date(2015, 7, 1)
#
# # printing dates
# print("The original range : " + str(test_date1) + " " + str(test_date2))
#
# # initializing K
# K = 7
#
# res_dates = [test_date1]
#
# # loop to get each date till end date
# while test_date1 != test_date2:
#     test_date1 += timedelta(days=1)
#     res_dates.append(test_date1)
#
# # random K dates from pack
# res = choices(res_dates, k=K)
#
# # printing
# print("K random dates in range : " + str(res))
#
#
#
#
