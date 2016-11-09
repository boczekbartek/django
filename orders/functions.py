from datetime import time, timedelta
from math import floor
import math
from datetime import datetime


def AfterComa(fl):
    return fl - floor(fl)


def generate_timetable(first_del_time=10, last_del_time=20, dels_per_hour=2):
    #first_del_time & last_del_time format is followieng: 8.30 or 20.15 etc.
    orders_num = (last_del_time - first_del_time) * dels_per_hour # delivery number during all dat
    deliv_timetable = []     #inicialization of timetable container
    #inicialization of date, year,month,day = whatever
    date = datetime(month=1, year=2016, day=1, hour=int(floor(first_del_time)), minute=int(AfterComa(last_del_time)))

    for i in range(0, int(orders_num)+1):
        deliv_timetable.append(date)
        date += timedelta(0, minutes=(60/dels_per_hour))

    return deliv_timetable

def isTimeValid(timee):
        if (timee + timedelta(0,minutes=-15)).time() > datetime.now().time():
            return True
        else:
            return False
    # except Exception:
    #     print ("Invalid Value in time checking function, false returned")
    #     return False

# a = generate_timetable(8.00,20.00,4)
# for i in a:
#     print i.time()
#
#
# t = datetime(month=1, year=2016, day=1, hour=13, minute=20)
# if isTimeValid(t):
#     print (str(t.time()) + "is valid")
# else:
#     print (str(t.time()) + " is invalid")
