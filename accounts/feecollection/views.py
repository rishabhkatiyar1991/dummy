from django.conf import settings
from django.shortcuts import render, redirect
#from djnago.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.

def index(request):
    return render(request, 'index.html')

def feelogin(request):
    if request.user.authenticate():
        return redirect('fee_dashbord')
    context = {}
    if request.method == 'POST':
        uname = request.POST["username"]
        pwd = request.POST["password"]
        user = authenticate(request, username = uname, password = pwd)
        #print(user)
        if user is not None:
            #authenticate.login(request, user)
            return redirect(fee_dashbord)
        else:
            context['error'] = {"Provide Valid Credentioal"}
            return redirect(request, 'index.html', context)
    else:
        return redirect(request, 'index.html')
    #return redirect(login)

#   @login_required(login_url='/index/')
def fee_dashbord(request):
    if not request.user.authenticate():
        return redirect(index)
    return render(request, 'fee_dashbord.html')

def feefinddate(request):
    #print('feeeeee');
    if request.method == 'POST':
        feefinddate = request.POST["feefinddate"]
        #print(feefinddate)
        today = datetime.date.today()
        #month = datetime.date.month()
        print(today)
        #N=2
        #print(month)
        if(feefinddate == 'next monday'):
            nextmonday=today+datetime.timedelta(days=-today.weekday(), weeks=1)     # monday of 1st week
            nexttus=today+datetime.timedelta(1-today.weekday(), weeks=2)     # tuesday of 2nd week of month
            saturday = today + datetime.timedelta(5 - today.weekday())  # print saturday of current weeks
            friday = today + datetime.timedelta((0 - today.weekday()) % 7)  # print next friday or next days, days will be start 0 to 6 (0=>monday and 6=>sunday)
            last_tuesday = today - datetime.timedelta(days= (today.weekday() - 1) % 7)  # print last tuesday if today(25-2-2020) is tuesday so print same day(25-2-2020)
            #pre_days = today - datetime.timedelta(days=N)  # for previous days
            #today += datetime.timedelta(22)         # count days like- tomorrow, next day

            print(nextmonday)
            print(nexttus)
            print(saturday)
            print(friday)
            print(last_tuesday)

            #print(pre_days)
        #elif(feefinddate == '1st saturday of next month'):
        #    nextmont=today+datetime.timedelta()
    return render(request, 'fee_dashbord.html')


def fee_logout(request):
    auth.logout(request)
    return redirect(index)

