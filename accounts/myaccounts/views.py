from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.backends.base import SessionBase
from django.contrib import auth
from django.contrib.auth.models import User
#from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.session import se
from django.urls import reverse
from .models import User, amount_details, student_details
from .forms import *
from django.contrib import messages
from django.conf import settings
import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        #request.session['username'] = username
        user = auth.authenticate(username = uname, password = pwd)
        #print(request.session['username'])
        #user = authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            context['user'] = user
            return redirect(success)
            #return render(request, 'success.html', context)
        else:
            context['error'] = "Provide valid credentials"
            return render(request, 'homee.html', context)
    else:
        return render(request, 'homee.html', {})
    #return HttpResponse("Hello")

#@login_required(login_url='/myaccounts/aclogin/')
@login_required(login_url='/myaccounts/home')
def success(request):
    #print(request.session['username'])
    #print(dir(request.session))
    #print(request.session.get("user"))
    #request.user = 'user'

    #context = getcontext()
    #return HttpResponseRedirect('success')
    print(request.session.keys())
    return render(request, 'success.html', {})
    #return redirect(request.POST.get('next', '/accounts/success/'))'username': request.session['username']
    #return redirect('/aclogin/?next=%s' % request.success)

#@login_required(login_url='/myaccounts/aclogin/')
def register(request):
    #print(request.user)
    #print(request.session['username'])
    context = {}

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            #if user.is_active:
            amt_date = datetime.datetime.now()
            session_time = form.cleaned_data['sdate']
            cour_year = form.cleaned_data['courseYear']
            reg_no = form.cleaned_data['regno']
            first_name = form.cleaned_data['firstname']
            last_name = form.cleaned_data['lastname']
            father_name = form.cleaned_data['fathername']
            agent_name = form.cleaned_data['agentrname']
            course = form.cleaned_data['course']
            amt_type = form.cleaned_data['amttype']
            amount = form.cleaned_data['amount']
            fee = form.cleaned_data['fee']
            commission = form.cleaned_data['commission']
            mobile = form.cleaned_data['mobile']
            org_name = form.cleaned_data['orgname']

            student_detail = student_details(amt_date = amt_date,session_time=session_time, cour_year=cour_year, reg_no=reg_no, first_name=first_name,last_name=last_name,
                                             father_name=father_name, agent_name=agent_name, course=course,amt_type=amt_type, amount=amount,fee=fee,
                                             commission=commission, mobile=mobile, org_name=org_name)
            student_detail.save()
                #context['error'] = "Provide valid credentials"
            messages.add_message(request, messages.SUCCESS, "You Have Successfully Stored Data!!!")
                #return HttpResponseRedirect(reverse('home'))'username': request.session['username']
            return render(request, 'register.html', {})
            #return HttpResponseRedirect(reverse('/'))
            # return redirect('home')
            #return render(request, 'homee.html', {})
            #return render(request, 'homee.html', context)
        else:
            context = {'form':StudentForm} #'username': request.session['username']
            return render(request, 'register.html', context)
    else:
        context = {'form': StudentForm}
        return render(request, 'register.html', context)


def feelist(request):
    context = {}
    stud_details = student_details.objects.all().order_by('-amt_date')
    print(stud_details)
    #context = {'username': request.session['username']}
    #return HttpResponseRedirect('feelist')
    context['stud_details'] = stud_details
    return render(request, 'feelist.html', {})

def details(request, id=None):
    context = {}
    stud_details = student_details.objects.get(id=id)
    print(stud_details)
    #context = {'username': request.session['username']}
    # return HttpResponseRedirect('feelist')
    context['stud_details'] = stud_details
    return render(request, 'details.html', {})


def editfee(request, id=None):
    context = {}
    stud_details = student_details.objects.get( id=id)

    form = StudentForm(request.POST or None)
    context = {
        'stud_details': stud_details,
        'firstname': stud_details.first_name,
        'form': form}
    print(stud_details)
    print(context)
    #context['stud_details'] = stud_details
    return render(request, 'editfee.html', context)

@login_required(login_url='/myaccounts/home')
def logout(request):
    if SessionBase.TEST_COOKIE_NAME not in request.session:
        for sesskey in request.session.keys():
            del request.session[sesskey]
            auth.logout(request)
    return redirect(home)
    # try:
    #     del request.session['username']
    #     if request.method == 'POST':
    #         logout(request)
    #     return render(request, '/aclogin.html', {})
    # except Exception as e:
    #     #pass
    #     print(e)
    # return render(request, '/aclogin.html', {})
    """del request.session['username']
    if request.method == 'POST':
        logout(request)
        del request.session['username']
        return render(request, '/aclogin.html', {})"""
        #return HttpResponseRedirect(reverse('/'))



"""def user_login(request):
    context = {}
    if request.method == "POST":
        pass
    else:
        return render(request, "myaccounts/aclogin.html", context)"""
