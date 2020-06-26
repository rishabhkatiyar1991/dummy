#from django.contrib.auth import authenticate, login, logout
#for login -----start-----
def login(request):
    context = {}
    #next = request.GET.get('next')
    #request.session['username'] = request.POST['username']
    #print(request.session['username'])
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        request.session['username'] = username
        #print(request.session['username'])
        user = authenticate(request, username = username, password = password)
        #print(user)
        #request.session['user'] = user
        #print(request.session['user'])
        #login(request, user)
        if user is not None:
            context['user'] = user
            #login(request, user)
            """if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('success'))"""
            #return HttpResponseRedirect(request.POST.get('next', 'success'))
            if user.is_active:
            #if request.GET.get('next', None):
                #return HttpResponseRedirect(request.GET['next'])
                #request.session['user'] = user
                request.session.set_expiry(500)
                return render(request, 'success.html', context)
            return HttpResponseRedirect(reverse('/aclogin'))
            #return HttpResponseRedirect('/aclogin')
            #return HttpResponseRedirect(request.GET['next'])
            """else:
                context['error'] = "Provide login"
                return render(request, 'aclogin.html', context)"""
        else:
            context['error'] = "Provide valid credentials"
            return render(request, 'aclogin.html', context)
    else:
        #return redirect(login)
        return render(request, 'aclogin.html', context)
    #return HttpResponse("Hello")
#-------------End----------------------