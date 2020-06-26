from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.sessions.backend.base import SessionBase
from django.contrib.auth.hashers import make_password
#from passlib.hash import pbkdf2_sha256
from dpsgsale.models import User, product_details
from dpsgsale.forms import *
import datetime

# Create your views here.

def login(request):
    context = {}
    #HttpResponse('hello')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        request.session['username'] = username
        #request.session.session_key = id

        user = authenticate(request, username = username, password = password)
        if user is not None:
            #context['user'] = user
            if user.is_active:
                request.session.set_expiry(1800)
                context = {'username': request.session['username']}
                return render(request, 'dashbord.html', context)
            return HttpResponseRedirect(reversed('/dlogin'))
            #return HttpResponseRedirect(reverse('/'))
        else:
            context['error'] = 'Provide valid Username or Password!!'
            return render(request, 'dlogin.html', context)
    else:
        #context = {'username': request.session['username']}
        return render(request, 'dlogin.html', context)

#@login_required(login_url='/dpsgsale/login/')
def dashbord(request):
    context = {'username' : request.session['username']}
    return render(request, 'dashbord.html', context)

def registration(request):
    context = {}
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid() and  User.is_active:
            user_name = form.cleaned_data['uname']
            first_name = form.cleaned_data['fname']
            last_name = form.cleaned_data['lname']
            password = form.cleaned_data['password']

            crew_password = make_password(password)
            #enc_password =(pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=36))

            user = User(username = user_name, first_name = first_name, last_name=last_name, password=crew_password)
            user.save()
            return redirect('registration')
            #return render(request, 'registration.html', {'username': request.session['username']})
        else:
            context = {'form': StudentForm, 'username': request.session['username']}
            return render(request, 'registration.html', context)
    else:
        context = {'form': StudentForm ,'username': request.session['username']}
        return render(request, 'registration.html', context)

def reglist(request):
    context= {}
    userdata = User.objects.all()
    #print(userdata)
    context = {'userdata': userdata,'username': request.session['username']}
    return render(request, 'reg_list.html', context)

def product(request):
    context= {}
    if request.method == 'POST':
        form = productForm(request.POST, request.FILES or None)
        #print(form)
        if form.is_valid():
            #print('hhhhhhhh')
            pro_date = datetime.datetime.now()
            user_id = request.POST['u_id']
            username = request.POST['u_name']
            fname = request.POST['fname']
            lname = request.POST['lname']
            class_name = form.cleaned_data['class_name']
            mobile = form.cleaned_data['mobile']
            price = form.cleaned_data['price']
            images = form.cleaned_data['images']

            prod_detail = product_details(pro_date = pro_date, user_id=user_id,username=username,first_name=fname,last_name=lname,
                                          class_name = class_name, mobile = mobile, price = price, pro_images=images)
            #print(prod_detail)
            prod_detail.save()
            #print(prod_detail)
            return redirect('product_list')
            #return render(request, 'product.html', {'username': request.session['username']})
        else:
            context = {'form': productForm, 'username': request.session['username']}
            return render(request, 'product.html', context)
    else:
        userdata = User.objects.get(username= request.session['username'])
        #print(userdata)
        context = {'userdata': userdata, 'form': productForm,'username': request.session['username']}
        return render(request, 'product.html', context)

def product_list(request):
    context={}
    pro_list = product_details.objects.filter(flag=0).order_by('-pro_date')
    userdata = User.objects.get(username=request.session['username'])
    #print(userdata)
    context = {'pro_list':pro_list,'username': request.session['username']}

    return render(request, 'product_list.html', context)

def sold_product(request, id=None):
   #print(id) exit()
    context = {}
    #pro_details = product_details.objects.get(id=id)
    if id is not None:
        userdata = User.objects.get(username=request.session['username'])

        update_data = product_details.objects.filter(id=id).update(flag='1',purch_userid=userdata.id, purch_username=userdata.username,
                                                                   purch_first_name=userdata.first_name,purch_last_name=userdata.last_name,
                                                                   purch_date=datetime.datetime.now())
        #update_data.save()
        print(update_data)
        #context = {'update_data': update_data, 'username': request.session['username']}
        return redirect('product_list')
        #return render(request, 'sold_productlist.html', context)
    #pro_details = product_details.objects.filter(id=id).update(purch_userid = pur_userid,purch_username=pur_usernm,purch_first_name=pur_fname,purch_last_name=pur_lname)
    #pur_data.save()
    #print(pro_details)
    else:
        #solddata = product_details.objects.filter(flag=1).order_by('-purch_date')
        context = {'username': request.session['username']}
        #context['update_data'] = update_data
        return render(request, 'product_list.html', context)

def sold_productlist(request):
    solddata = product_details.objects.filter(flag=1).order_by('-purch_date')
    context = {'solddata': solddata, 'username': request.session['username']}
    # context['update_data'] = update_data
    return render(request, 'sold_productlist.html', context)



def logout(request):
    """try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect("/")"""

    #for sesskey in request.session.keys():
        #del request.session[sesskey]
    #return logout(request)
    #if request.method == 'POST':
        #logout(request)
    del request.session['username']
    auth.logout(request)
    return HttpResponseRedirect('/dlogin')