from django.shortcuts import render
from .models import Pasta,Sauce,Dish,Additional_Ingredient
from django.http import Http404, HttpResponseRedirect

from django.conf.urls import url
import datetime
from django.utils import timezone
import fileinput
from django.urls import reverse





from datetime import time, timedelta
from math import floor
import math
from datetime import datetime

class Danie:
    def __init__(self,pastaa):
        self.makaron = pastaa


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

def isTimeValid(timee,latency = 30):
        #sprawdza czy zadany w agrumencie czas jest nadal wazny, czyli jest o minimum $latency wczesniej niz aktualny czas
        if (timee + timedelta(0,minutes=-latency)).time() > datetime.now().time():
            return True
        else:
            return False















def pasta (request):

    sauce=request.POST['choosed_sauce']

    all_pastas = Pasta.objects.all()

    return render (request,('orders/pasta.html'), {'all_pastas':all_pastas, 'sauce': sauce})



def sauce(request):
    all_sauces = Sauce.objects.all()
    return render(request, 'orders/sauce.html', {'all_sauces': all_sauces})

def ingredients(request):

    sauce=request.POST['choosed_sauce']
    pasta=request.POST['choosed_pasta']

    all_ingredients = Additional_Ingredient.objects.all()
    return render(request, 'orders/ingredients.html', {'all_ingredients': all_ingredients, 'sauce': sauce, 'pasta': pasta})

def add_ingredients(request):
    #tu ma byc zrobione dodawanie skladnikow do disha
    times = generate_timetable(10.00, 23.00, 3)
    stra = ""
    strb = ""
    y = [s for s in times if isTimeValid(s)]
    # for t in times:
    #     # stra = stra + str(t.time()) + '\n'
    #     if not isTimeValid(t):
    #         times.remove(t)
    #         stra = stra + str(t.time()) + '\n'
    # for t in times:
    #     strb = strb + str(t.time()) + '\n'

    return render(request, 'orders/timetable.html', {'log': stra, 'log2' :strb ,'timetable': y, 'actual_time': timezone.now()})

        # return HttpResponse("<h2>Details for Dish id:" + str(dish_id) + "</h2>")
def overview(request):
    time = request.POST['timee']
    return render(request, 'orders/overview.html',{'del_time':time})

# def timetable(request):
#
#     times = generate_timetable(10.00,20.00,2)
#     return render(request, 'orders/timetable.html', {'timetable': times, 'actual_time': datetime.now().time()})

def order (request):
    #wyczyść danie i wszystkie cache a na
    #dodaj zamowienie do widoku zamowien w panelu administratora

    return render(request, 'orders/order.html')

